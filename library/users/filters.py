from django.contrib import admin

from core.constants import UserConstants


class HasRentedBooksFilter(admin.SimpleListFilter):
    """
    Кастомный фильтр для админ-панели читателей. Позволяет фильтровать
    пользователей, которые в данный момент имеют книги на руках.
    """

    title = UserConstants.HAS_BOOKS_RENTED.value
    parameter_name = 'has_rented_books'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Да'),
            ('no', 'Нет'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(books__isnull=False)
        if self.value() == 'no':
            return queryset.filter(books__isnull=True)
        return queryset
