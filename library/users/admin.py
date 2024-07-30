from django.contrib import admin

from core.constants import UserConstants
from users.filters import HasRentedBooksFilter
from users.forms import ReaderAdminForm, LibrarianAdminForm
from users.models import Librarian, Reader, LibExtraFields, ReaderExtraFields


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = (
        "username", "first_name", "last_name", "table_number")
    form = LibrarianAdminForm

    @admin.action(description=UserConstants.TABLE_NUMBER.value)
    def table_number(self, obj):
        return obj.lib_extra_fields.table_number

    def save_model(self, request, obj, form, change):
        instance = form.instance
        if change:
            LibExtraFields.objects.filter(
                user=instance
            ).update(table_number=form.data.get("table_number"))
            instance.save()


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = (
        "username", "first_name", "last_name", "address", "ever_rented_a_book",
        "has_rented_books"
    )
    form = ReaderAdminForm
    list_filter = ("ever_rented_a_book", HasRentedBooksFilter)

    @admin.display(description=UserConstants.ADDRESS.value)
    def address(self, obj):
        return obj.reader_extra_fields.address

    @admin.display(description=UserConstants.HAS_BOOKS_RENTED.value,
                   boolean=True)
    def has_rented_books(self, obj):
        return len(obj.books.all()) > 0

    def save_model(self, request, obj, form, change):
        instance = form.instance
        if change:
            ReaderExtraFields.objects.filter(
                user=instance
            ).update(address=form.data.get("address"))
            instance.save()

