from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView

from books.forms import BookCreateForm
from books.models import Book
from users.views import User


class BooksListView(ListView):
    model = Book
    template_name = "books/index.html"
    context_object_name = "books"
    paginate_by = 10


class MyBooksListView(BooksListView):
    ordering = "title"

    def get_queryset(self):
        return super().get_queryset().filter(reader=self.request.user)


class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy("books:index")
    template_name = "books/add_book.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_librarian:
            raise PermissionDenied(
                "У вас нет прав для добавления книг в картотеку."
            )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)


class LibrarianUsersListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "users"
    paginate_by = 10


@login_required
def rent_a_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        if book.is_borrowed:
            raise PermissionDenied(
                "Вы не можете взять эту книгу в аренду, т.к. она уже "
                "занята другим читателем."
            )
        else:
            book.reader = request.user
            book.is_borrowed = True
            book.borrowed_at = now()
        book.save()
    return redirect("books:index")


@login_required
def return_a_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        if book.is_borrowed and book.reader == request.user:
            book.reader = None
            book.is_borrowed = False
            book.borrowed_at = None
            book.save()
    return redirect("books:index")
