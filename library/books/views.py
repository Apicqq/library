from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from core.constants import Errors
from books.book_management import manage_books
from books.forms import BookCreateForm
from books.models import Book
from users.models import Reader


class BooksListView(ListView):
    """
    Представление для списка всех книг, используется на главной странице
    веб-приложения.
    """

    model = Book
    template_name = "books/index.html"
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.select_related("reader").all()


class MyBooksListView(BooksListView):
    """
    Список книг, которые текущий пользователь взял на руки.
    """

    ordering = "title"

    def get_queryset(self):
        return Book.objects.select_related("reader").filter(
            reader=self.request.user
        )


class BookCreateView(CreateView):
    """
    Представление для добавления книги библиотекарем через веб-интерфейс.
    """

    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy("books:index")
    template_name = "books/add_book.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_librarian:
            raise PermissionDenied(Errors.NOT_AUTHORIZED_TO_RENT.value)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)


class LibrarianDebtorsListView(ListView):
    """
    Список должников, которые взяли книги на руки в библиотеке.
    """

    model = Reader
    template_name = "books/debtors.html"
    context_object_name = "users"
    paginate_by = 10


@login_required
def rent_a_book(request, pk):
    """
    Выдать книгу на руки пользователю.
    """
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        if not manage_books(request, book, "RENT"):
            raise PermissionDenied(Errors.BOOK_IS_RENTED.value)
        else:
            return redirect(request.META.get("HTTP_REFERER"))


@login_required
def return_a_book(request, pk):
    """
    Вернуть книгу в библиотеку.
    """
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        if not manage_books(request, book, "RETURN"):
            raise PermissionDenied(Errors.BOOK_NOT_RENTED.value)
    return redirect(request.META.get("HTTP_REFERER"))
