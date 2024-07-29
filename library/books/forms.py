from django import forms

from books.models import Book


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["title", "author", "genre", "year", "cover"]