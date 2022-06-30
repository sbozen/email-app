from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MailSettings, User


# @receiver(post_save, sender=User)
# def save_user(sender, instance, created, **kwargs):
#     print("come to save_user")
#     print(instance.id)
#     if created:
#         print('created')
#         instance = MailSettings.objects.create(is_set=False,
#                                                email_address=instance.email,
#                                                app_password="None", smtp_server=0, smtp_port=0,
#                                                user=instance)
#         instance.save()
#     print('-----------------------------------------------------')
