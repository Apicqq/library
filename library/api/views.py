from http import HTTPStatus

from django.utils.timezone import now
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.permissions import IsRenterReadOnly
from api.serializers import BookSerializer, BookOnHandsSerializer
from books.models import Book


class BookListViewSet(GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(responses={200: BookSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: BookOnHandsSerializer(many=True),
                                    400: 'Book is already borrowed'})
    @action(methods=['post'], detail=True)
    def rent(self, request, pk=None):
        book = self.get_object()
        if book.is_rented:
            return Response({'error': 'Book is already borrowed'},
                            status=HTTPStatus.BAD_REQUEST)
        book.is_rented = True
        book.rented_at = now()
        book.reader = request.user
        book.reader.ever_rented_a_book = True
        book.reader.save()
        book.save()
        return Response({'success': 'Book borrowed successfully'},
                        status=HTTPStatus.OK)

    @swagger_auto_schema(
        responses={
            HTTPStatus.OK.value: 'Book returned successfully',
            HTTPStatus.BAD_REQUEST.value: 'Book is not borrowed',
            HTTPStatus.FORBIDDEN.value: 'Book is not borrowed by request user'
        }
    )
    @action(methods=['post'], detail=True,
            permission_classes=[IsRenterReadOnly])
    def return_book(self, request, pk=None):
        book = self.get_object()
        if not book.is_rented:
            return Response({'error': 'Book is not borrowed'}
                            , HTTPStatus.BAD_REQUEST)
        book.is_rented = False
        book.rented_at = None
        book.reader = None
        book.save()
        return Response({'success': 'Book returned successfully'},
                        status=HTTPStatus.OK)

    @action(methods=['get'], detail=False)
    def get_book_on_hands(self, request):
        book_on_hands = Book.objects.filter(
            reader=request.user,
            is_rented=True
        )
        serializer = BookOnHandsSerializer(book_on_hands, many=True)
        return Response(serializer.data)
