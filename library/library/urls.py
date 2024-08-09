from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls

from core import views


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("books.urls")),
        path("users/", include("users.urls")),
        path("api/", include("api.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)


handler404 = views.page_not_found

handler500 = views.internal_error

handler403 = views.csrf_failure
