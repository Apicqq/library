from django.contrib import admin

from users.filters import HasRentedBooksFilter
from users.forms import RegistrationForm
from users.models import Librarian, Reader


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = (
        "username", "first_name", "last_name", "table_number")
    form = RegistrationForm

    @admin.action(description="Табельный номер")
    def table_number(self, obj):
        return obj.lib_extra_fields.table_number


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = (
        "username", "first_name", "last_name", "address", "ever_rented_a_book",
        "has_rented_books"
    )
    form = RegistrationForm
    list_filter = ("ever_rented_a_book", HasRentedBooksFilter)

    @admin.display(description="Адрес проживания")
    def address(self, obj):
        return obj.reader_extra_fields.address

    @admin.display(description="Есть книги на руках", boolean=True)
    def has_rented_books(self, obj):
        return len(obj.books.all()) > 0
