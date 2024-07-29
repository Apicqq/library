from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User, ReaderExtraFields, LibExtraFields


@receiver(post_save, sender=User, dispatch_uid="create_user_address")
def populate_extra_fields(sender, instance, created, **kwargs):
    if created:
        if instance.role == "READER":
            created_data = ReaderExtraFields.objects.create(
                user=instance,
                address=instance.address
            )
            created_data.save()
        else:
            created_data = LibExtraFields.objects.create(
                user=instance,
                table_number=instance.table_number
            )
            created_data.save()
