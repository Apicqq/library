from django.contrib.auth.models import AbstractUser
from django.db import models


class Librarian(AbstractUser):
    table_number = models.CharField(
        "Табельный номер",
        max_length=10,
    )

    class Meta:
        verbose_name = "Библиотекарь"
        verbose_name_plural = "Библиотекари"

    def __str__(self):
        return self.username


class Reader(AbstractUser):
    address = models.CharField(
        "Адрес проживания",
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return self.username
