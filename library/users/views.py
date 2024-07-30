from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from users.forms import RegistrationForm

User = get_user_model()


class SignUpView(CreateView):
    """
    Контроллер для регистрации пользователей через веб-интерфейс.
    """

    form_class = RegistrationForm
    success_url = reverse_lazy("users:login")
    template_name = "registration/registration_form.html"


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра информации о пользователе через веб-интерфейс.
    """

    model = User
    template_name = "users/user_detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(
            **context,
            profile=self.get_object(),
        )


def get_dynamic_fields(request):
    """
    Контроллер, использующийся для AJAX-скрипта.
    Позволяет динамически скрывать поля неактуальные поля во время регистрации.
    Если пользователь — читатель, то скрывает поле "адрес", и наоборот.
    """
    role = request.GET.get('role')
    if role == "READER":
        fields = {"address": "visible", "tab_number": "hidden"}
    elif role == "LIBRARIAN":
        fields = {"address": "hidden", "tab_number": "visible"}
    else:
        fields = {"address": "hidden", "tab_number": "hidden"}
    return JsonResponse(fields)
