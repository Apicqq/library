import factory
from factory.django import DjangoModelFactory
from faker import Faker

from books.models import Book
from users.models import User, Reader, Librarian, ReaderExtraFields, \
    LibExtraFields


class BaseUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class ReaderFactory(BaseUserFactory):
    class Meta:
        model = Reader

    role = User.Roles.READER

    @factory.post_generation
    def set_address(self, create, extracted, **kwargs):
        if create:
            created_data = ReaderExtraFields.objects.create(
                user=self, address=Faker(locale="ru_RU").address()
            )
            created_data.save()


class LibrarianFactory(BaseUserFactory):
    class Meta:
        model = Librarian

    role = User.Roles.LIBRARIAN

    @factory.post_generation
    def set_address(self, create, extracted, **kwargs):
        if create:
            created_data = LibExtraFields.objects.create(
                user=self,
                table_number=Faker(locale="ru_RU").pyint(min_value=1)
            )
            created_data.save()


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", locale="ru_RU")
    author = factory.Faker("name", locale="ru_RU")
    genre = factory.Faker("word", locale="ru_RU")
    year = factory.Faker("year", locale="ru_RU")
    cover = factory.django.ImageField(color="blue", width=640, height=480)
