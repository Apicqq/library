from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User, ReaderExtraFields, LibExtraFields


@receiver(post_save, sender=User, dispatch_uid="create_user_address")
def populate_extra_fields(sender, instance, created, **kwargs):
    """
    Сингал, использующийся для наполнения данными таблиц для прокси-моделей
    читателя и библиотекаря.
    """
    if created:
        if instance.is_reader:
            obj, created = ReaderExtraFields.objects.update_or_create(
                user=instance, address=instance.address
            )
        else:
            obj, created = LibExtraFields.objects.update_or_create(
                user=instance, table_number=instance.table_number
            )
