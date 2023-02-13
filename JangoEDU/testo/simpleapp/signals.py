from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import mail_admins
from .models import Product


@receiver(post_save, sender=Product)
def notify_admin_product(sender, instance, created, **kwargs):
    if created:
        subject = f'Продукт создан {instance.name} {instance.category}'
    else:
        subject = f'Продукт изменен {instance.name} {instance.category}'

    mail_admins(
        subject=subject,
        message=instance.description,
    )


@receiver(post_delete, sender=Product)
def notify_admin_product(sender, instance, **kwargs):
    subject = f'Продукт удален из списка {instance.name} {instance.category}'

    mail_admins(
        subject=subject,
        message=instance.description,
    )
