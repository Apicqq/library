from django.utils.timezone import now
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, DateTimeField

from books.models import Book


class BookSerializer(ModelSerializer):
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
        return (now() - obj.rented_at).days
