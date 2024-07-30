from django.core.management.base import BaseCommand

from core.data_factories.factories import (
    BookFactory,
    ReaderFactory,
    LibrarianFactory,
)


class Command(BaseCommand):
    """
    Команда, позволяющая добавлять в тестовую базу данных фикстуры
    существующих моделей, будь то книга, читатель или библиотекарь через CLI.
    """

    help = "Добавляет в тестовую базу данных фикстуры."

    def handle(self, *args, **options):
        books, amount = options.get("books"), options.get("amount")

        if books:
            BookFactory.create_batch(amount)
            return self.stdout.write(
                self.style.SUCCESS(
                    f"{amount} фикстур для книг добавлено в БД."
                )
            )

        readers, librarians = options.get("readers"), options.get("librarians")

        if readers:
            ReaderFactory.create_batch(amount)
            return self.stdout.write(
                self.style.SUCCESS(
                    f"{amount} фикстур для читателей добавлено в БД."
                )
            )

        if librarians:
            LibrarianFactory.create_batch(amount)
            return self.stdout.write(
                self.style.SUCCESS(
                    f"{amount} фикстур для библиотекарей добавлено в БД."
                )
            )

    def add_arguments(self, parser):
        parser.add_argument(
            "-b",
            "--books",
            action="store_true",
            help="Фикстуры книг для добавления в тестовую базу данных",
        )
        parser.add_argument(
            "-r",
            "--readers",
            action="store_true",
            help="Фикстуры читателей для добавления в тестовую базу данных",
        )
        parser.add_argument(
            "-l",
            "--librarians",
            action="store_true",
            help="Фикстуры библиотекарей для добавления в тестовую базу данных",
        )
        parser.add_argument(
            "-a",
            "--amount",
            type=int,
            default=10,
            help="Количество фикстур для добавления в тестовую базу данных",
        )
