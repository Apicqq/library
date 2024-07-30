from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.constants import UserConstants

class LibrarianManager(BaseUserManager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            role=User.Roles.LIBRARIAN
        )


class ReaderManager(BaseUserManager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            role=User.Roles.READER
        )


class User(AbstractUser):
    class Roles(models.TextChoices):
        LIBRARIAN = "LIBRARIAN", UserConstants.LIBRARIAN.value
        READER = "READER", UserConstants.READER.value

    base_type = Roles.READER

    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=base_type
    )
    ever_rented_a_book = models.BooleanField(
        default=False,
        verbose_name=UserConstants.EVER_RENTED_A_BOOK.value,
    )

    @property
    def is_librarian(self):
        return self.role == "LIBRARIAN"

    @property
    def is_reader(self):
        return self.role == "READER"

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class LibExtraFields(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    table_number = models.IntegerField(default=0)


class Librarian(User):
    objects = LibrarianManager()

    base_type = User.Roles.LIBRARIAN

    class Meta:
        verbose_name = UserConstants.LIBRARIAN.value
        verbose_name_plural = UserConstants.LIBRARIANS.value
        proxy = True

    @property
    def lib_extra_fields(self):
        return self.libextrafields


class ReaderExtraFields(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(
        UserConstants.ADDRESS.value,
        max_length=100,
        blank=True,
        null=True,
    )


class Reader(User):
    objects = ReaderManager()

    base_type = User.Roles.READER

    class Meta:
        verbose_name = UserConstants.READER.value
        verbose_name_plural = UserConstants.READERS.value
        proxy = True

    @property
    def reader_extra_fields(self):
        return self.readerextrafields
