from django.urls import include, path

from users.views import SignUpView, UserDetailView, get_dynamic_fields

app_name = "users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("registration/", SignUpView.as_view(), name="registration"),
    path("<slug:username>/", UserDetailView.as_view(), name="profile"),
    path(
        "ajax/get_dynamic_fields/",
        get_dynamic_fields,
        name="get_dynamic_fields",
    ),
]
