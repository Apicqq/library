"""Константы, использующиеся в проекте."""

from enum import Enum


class BookConstants(str, Enum):
    """Константы для модели Книги."""

    TITLE = "Название"
    AUTHOR = "Автор"
    GENRE = "Жанр"
    YEAR = "Год издания"
    COVER = "Обложка"
    IS_BORROWED = "Книга взята в прочтение"
    BORROWED_AT = "Дата взятия в прочтение"
    READER = "Читатель"
    BOOK = "Книга"
    BOOKS = "Книги"
    ADDED_AT = "Книга добавлена в картотеку"
    RENTED_SUCCESSFULLY = "Книга успешна взята в аренду"
    RETURNED_SUCCESSFULLY = "Книга успешна возвращена"


class Errors(str, Enum):
    """Константы текстовых сообщений об ошибках."""

    NOT_AUTHORIZED_TO_RENT = "У вас нет прав для добавления книг в картотеку."
    BOOK_IS_RENTED = (
        "Вы не можете взять эту книгу в аренду, т.к. она уже "
        "занята другим читателем."
    )
    INVALID_BOOK_YEAR = "Год выпуска книги не может быть больше текущего."
    BOOK_NOT_RENTED = "Эта книга не взята в прочтение."
    ACTION_NOT_PERMITTED = "Действие недоступно для вас."


class UserConstants(str, Enum):
    """Константы, использующиеся для моделей Пользователей."""

    LIBRARIAN = "Библиотекарь"
    LIBRARIANS = "Библиотекари"
    READER = "Читатель"
    READERS = "Читатели"
    FIRST_NAME = "Имя"
    LAST_NAME = "Фамилия"
    TABLE_NUMBER = "Табельный номер"
    ADDRESS = "Адрес проживания"
    HAS_BOOKS_RENTED = "Есть книги на руках"
    ROLE = "Роль"
    NON_REQUIRED_FIELD = "Необязательное поле"
    CHOOSE_YOUR_ROLE = "Выберите роль пользователя."
    FIELD_FOR_READERS = "Для читателей."
    FIELD_FOR_LIBRARIANS = "Для библиотекарей."
    EVER_RENTED_A_BOOK = "Когда-либо брал книгу напрокат"
