from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from books.models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(SimpleHistoryAdmin):
    list_display = (
        "title",
        "author",
        "genre",
        "year",
        "cover",
        "is_borrowed",
        "borrowed_at",
        "reader",
    )
    list_filter = ("is_borrowed",)
