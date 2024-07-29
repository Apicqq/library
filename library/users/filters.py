from django.contrib import admin


class HasRentedBooksFilter(admin.SimpleListFilter):
    title = 'Есть книги на руках'
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
