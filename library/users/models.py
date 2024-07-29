from django.contrib.auth.models import AbstractUser
from django.db import models


class LibrarianManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            role=User.Roles.LIBRARIAN
        )


class ReaderManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            role=User.Roles.READER
        )


class User(AbstractUser):
    class Roles(models.TextChoices):
        LIBRARIAN = 'LIBRARIAN', 'Библиотекарь'
        READER = 'READER', 'Читатель'

    base_type = Roles.READER

    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=base_type
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


class LibExtraFields(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    table_number = models.IntegerField(default=0)


class Librarian(User):
    objects = LibrarianManager()

    base_type = User.Roles.LIBRARIAN

    class Meta:
        verbose_name = "Библиотекарь"
        verbose_name_plural = "Библиотекари"
        proxy = True

    @property
    def lib_extra_fields(self):
        return self.libextrafields


class ReaderExtraFields(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(
        "Адрес проживания",
        max_length=100,
        blank=True,
        null=True,
    )


class Reader(User):
    objects = ReaderManager()

    base_type = User.Roles.READER

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
        proxy = True

    @property
    def reader_extra_fields(self):
        return self.readerextrafields
