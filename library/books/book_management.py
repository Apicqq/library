from django.utils.timezone import now

from books.models import Book


def manage_books(request, book: Book, action: str):
    """Дать книгу напрокат либо вернуть её в библиотеку."""
    user = request.user
    match action:
        case "RENT":
            if book.is_rented:
                return False
            else:
                save_book_to_db(
                    book,
                    request,
                    user,
                    action,
                )
            return True
        case "RETURN":
            if not book.is_rented:
                return False
            if book.is_rented and book.reader == request.user:
                save_book_to_db(
                    book,
                    request,
                    user,
                    action,
                )
            return True


def save_book_to_db(book, request, user, action):
    match action:
        case "RENT":
            book.is_rented = True
            book.rented_at = now()
            book.reader = request.user
            user.ever_rented_a_book = True
            user.ever_rented_a_book = True
            book.save()
            user.save()
        case "RETURN":
            book.reader = None
            book.is_rented = False
            book.rented_at = None
            book.save()
