from django import forms

from books.models import Book


class BookCreateForm(forms.ModelForm):
    """Форма для создания книги библиотекарем через веб-интерфейс."""

    class Meta:
        model = Book
        fields = ["title", "author", "genre", "year", "cover"]
