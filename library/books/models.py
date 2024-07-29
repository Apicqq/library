from django.db import models


class Book(models.Model):
    title = models.CharField("Название", max_length=100)
    author = models.CharField("Автор", max_length=100)
    genre = models.CharField("Жанр", max_length=100)
    year = models.IntegerField("Год издания")
    cover = models.ImageField("Обложка", upload_to="covers/")
    is_borrowed = models.BooleanField(
        "Книга взята в прочтение",
        default=False
    )
    borrowed_at = models.DateTimeField(
        "Дата взятия книги",
        null=True,
        blank=True
    )
    reader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="books",
        verbose_name="Читатель",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title
