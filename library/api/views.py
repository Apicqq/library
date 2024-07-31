from http import HTTPStatus

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.permissions import IsRenterReadOnly
from api.serializers import BookSerializer, BookOnHandsSerializer
from books.book_management import manage_books
from books.models import Book
from core.constants import BookConstants, Errors


class BookListViewSet(GenericViewSet):
    """Вьюсет для всех эндпоинтов, связанных с книгами."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(responses={200: BookSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        """Вернуть список всех книг в библиотеке."""
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            HTTPStatus.OK.value: BookOnHandsSerializer(many=True),
            HTTPStatus.BAD_REQUEST.value: Errors.BOOK_IS_RENTED.value,
        }
    )
    @action(methods=["post"], detail=True)
    def rent(self, request, pk=None):
        """Выдать книгу на руки пользователю."""
        book = self.get_object()
        if not manage_books(request, book, "RENT"):
            return Response(
                {"error": Errors.BOOK_IS_RENTED.value},
                status=HTTPStatus.BAD_REQUEST,
            )
        return Response(
            {"success": BookConstants.RENTED_SUCCESSFULLY.value},
            status=HTTPStatus.OK,
        )

    @swagger_auto_schema(
        responses={
            HTTPStatus.OK.value: BookConstants.RENTED_SUCCESSFULLY.value,
            HTTPStatus.BAD_REQUEST.value: Errors.BOOK_IS_RENTED.value,
            HTTPStatus.FORBIDDEN.value: Errors.ACTION_NOT_PERMITTED.value,
        }
    )
    @action(
        methods=["post"], detail=True, permission_classes=[IsRenterReadOnly]
    )
    def return_book(self, request, pk=None):
        """Вернуть книгу в библиотеку."""
        book = self.get_object()
        if not manage_books(request, book, "RETURN"):
            return Response(
                {"error": Errors.BOOK_NOT_RENTED.value}, HTTPStatus.BAD_REQUEST
            )
        return Response(
            {"success": BookConstants.RETURNED_SUCCESSFULLY.value},
            status=HTTPStatus.OK,
        )

    @action(methods=["get"], detail=False)
    def get_book_on_hands(self, request):
        """Получить список книг на руках у пользователя."""
        book_on_hands = Book.objects.filter(
            reader=request.user, is_rented=True
        )
        serializer = BookOnHandsSerializer(book_on_hands, many=True)
        return Response(serializer.data)
