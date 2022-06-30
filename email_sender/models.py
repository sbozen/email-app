from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class MailSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=50)
    app_password = models.CharField(max_length=50)
    smtp_server = models.CharField(max_length=50)
    smtp_port = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_set = models.BooleanField(default=False)

    def __str__(self):
        return self.email_address
