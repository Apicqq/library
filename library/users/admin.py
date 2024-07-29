from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Librarian, Reader


#
#
@admin.register(Librarian)
class LibrarianAdmin(UserAdmin):
    readonly_fields = ("table_number",)
    list_display = ("username", "first_name", "last_name", "table_number")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Персональная информация",
         {"fields": ("first_name", "last_name", "email", "table_number")}),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    @admin.action(description="Табличный номер")
    def table_number(self, obj):
        return obj.lib_extra_fields.table_number


@admin.register(Reader)
class ReaderAdmin(UserAdmin):
    readonly_fields = ("address",)
    list_display = ("username", "first_name", "last_name", "address",)

    @admin.action(description="Адрес проживания")
    def address(self, obj):
        return obj.reader_extra_fields.address

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Персональная информация",
         {"fields": ("first_name", "last_name", "email", "address")}),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )