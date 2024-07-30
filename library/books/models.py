from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now
from simple_history.models import HistoricalRecords

from books.validators import validate_book_year
from core.constants import BookConstants


class Book(models.Model):
    """Модель для хранения информации о книгах в библиотеке."""

    title = models.CharField(BookConstants.TITLE.value, max_length=100)
    author = models.CharField(BookConstants.AUTHOR.value, max_length=100)
    genre = models.CharField(BookConstants.GENRE.value, max_length=100)
    year = models.IntegerField(
        BookConstants.YEAR.value,
        validators=[
            validate_book_year,
            MinValueValidator(0),
            MaxValueValidator(now().year),
        ],
    )
    cover = models.ImageField(
        BookConstants.COVER.value, upload_to="covers/", blank=True, null=True
    )
    added_at = models.DateTimeField(
        BookConstants.ADDED_AT.value, auto_now_add=True
    )
    is_rented = models.BooleanField(
        BookConstants.IS_BORROWED.value, default=False
    )
    rented_at = models.DateTimeField(
        BookConstants.BORROWED_AT.value, null=True, blank=True
    )
    reader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="books",
        verbose_name=BookConstants.READER.value,
        blank=True,
        null=True,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = BookConstants.BOOK.value
        verbose_name_plural = BookConstants.BOOKS.value
        ordering = ["title"]

    def __str__(self):
        return self.title
