from django.contrib import admin
from .models import User, MailSettings
admin.site.register(User)
admin.site.register(MailSettings)

# Register your models here.
