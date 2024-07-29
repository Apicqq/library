# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from users.forms import RegistrationForm

User = get_user_model()


class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("users:login")
    template_name = "registration/registration_form.html"


class UserDetailView(LoginRequiredMixin, DetailView):
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
    role = request.GET.get('role')
    if role == "READER":
        fields = {"address": "visible", "tab_number": "hidden"}
    elif role == "LIBRARIAN":
        fields = {"address": "hidden", "tab_number": "visible"}
    else:
        fields = {"address": "hidden", "tab_number": "hidden"}
    return JsonResponse(fields)
