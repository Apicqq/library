from django.urls import path

from books.views import BooksListView, rent_a_book, return_a_book, MyBooksListView, BookCreateView

app_name = "books"

urlpatterns = [
    path("", BooksListView.as_view(), name="index"),
    path("my_books/", MyBooksListView.as_view(), name="my_books"),
    path("rent_a_book/<int:pk>/", rent_a_book, name="rent"),
    path("return_a_book/<int:pk>/", return_a_book, name="return"),
    path("add_book/", BookCreateView.as_view(), name="add_book"),
]