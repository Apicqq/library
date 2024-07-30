from django.utils.timezone import now
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, DateTimeField

from books.models import Book


class BookSerializer(ModelSerializer):
    """Сериалайзер, использующийся для получения всего списка книг."""
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "genre",
            "year",
        )


class BookOnHandsSerializer(ModelSerializer):
    """
    Сериалайзер, использующийся для получения списка книг на руках у
    должника.
    """

    borrowed_at = DateTimeField(
        read_only=True,
        format="%d-%m-%Y %H:%M:%S",

    )
    days_since_borrowed = SerializerMethodField(
        read_only=True,
    )

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "borrowed_at",
            "days_since_borrowed",
        )

    def get_days_since_borrowed(self, obj):
        """
        Возвращает количество дней, прошедших с даты выдачи книги.
        """
        return (now() - obj.rented_at).days
