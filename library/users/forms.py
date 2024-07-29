from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=User.Roles.choices,
        label=_('Роль'),
        help_text=_('Выберите роль пользователя.'),
    )
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='Необязательное поле.',
                                 label=_('Имя'))
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='Необязательное поле.',
                                label=_('Фамилия'))
    email = forms.EmailField(max_length=254,
                             help_text='Введите актуальный'
                                       ' адрес электронной почты.',
                             label=_('Электронная почта'))
    address = forms.CharField(max_length=100, required=False,
                              help_text='Необязательное поле.',
                              label=_('Адрес проживания'),)
    table_number = forms.IntegerField(required=False,
                                      help_text='Необязательное поле.',
                                      label=_('Табельный номер'))

    def save(self, commit=True):
        match self.cleaned_data["role"]:
            case "READER":
                self.instance.address = self.cleaned_data.get("address")
            case "LIBRARIAN":
                self.instance.table_number = self.cleaned_data.get(
                    "table_number"
                )
        return super(RegistrationForm, self).save(commit)

    class Meta:
        model = User
        fields = [
            "role",
            'username',
            'first_name',
            'last_name',
            "address",
            "table_number",
            'email',
            'password1',
            'password2',
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_active')
        widgets = {
            'password': forms.PasswordInput()

        }
