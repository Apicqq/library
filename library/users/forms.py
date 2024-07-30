from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm
from django.utils.translation import gettext_lazy as _

from core.constants import UserConstants

User = get_user_model()


class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=User.Roles.choices,
        label=_(UserConstants.ROLE),
        help_text=_(UserConstants.CHOOSE_YOUR_ROLE),
    )
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text=_(UserConstants.NON_REQUIRED_FIELD),
                                 label=_(UserConstants.FIRST_NAME))
    last_name = forms.CharField(max_length=30, required=False,
                                help_text=_(UserConstants.NON_REQUIRED_FIELD),
                                label=_(UserConstants.LAST_NAME))
    address = forms.CharField(max_length=100, required=False,
                              help_text=_(UserConstants.FIELD_FOR_READERS),
                              label=_(UserConstants.ADDRESS), )
    table_number = forms.IntegerField(required=False,
                                      help_text=_(
                                          UserConstants.FIELD_FOR_LIBRARIANS),
                                      label=_(UserConstants.TABLE_NUMBER))

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


class ReaderAdminForm(BaseUserCreationForm):
    address = forms.CharField(max_length=100, required=False,
                              help_text=_(UserConstants.FIELD_FOR_READERS),
                              label=_(UserConstants.ADDRESS), )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.initial:
            self.fields[
                "address"].initial = self.instance.reader_extra_fields.address
            self.fields["password1"].required = False
            self.fields["password2"].required = False

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "address",
            "email",
            "password1",
            "password2",
        ]


class LibrarianAdminForm(BaseUserCreationForm):
    table_number = forms.IntegerField(required=False,
                                      help_text=_(
                                          UserConstants.FIELD_FOR_LIBRARIANS),
                                      label=_(UserConstants.TABLE_NUMBER))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.initial:
            self.fields[
                "table_number"].initial = self.instance.lib_extra_fields.table_number
            self.fields["password1"].required = False
            self.fields["password2"].required = False

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "table_number",
            "email",
            "password1",
            "password2",
        ]
