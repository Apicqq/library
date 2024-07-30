from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from books.models import Book


@admin.register(Book)
class BookAdmin(SimpleHistoryAdmin):
    """Базовая админ панель для модели Книг."""

    list_display = (
        "title",
        "author",
        "genre",
        "year",
        "cover",
        "added_at",
        "is_rented",
        "rented_at",
        "reader",
    )
    list_filter = ("is_rented",)
