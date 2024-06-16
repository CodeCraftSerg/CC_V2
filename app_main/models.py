from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=75, unique=False, null=False)
    email = models.EmailField(max_length=320, unique=False, null=True)
    phone = models.CharField(max_length=20, null=True, unique=False)
    message = models.TextField(max_length=500, null=True, unique=False)

    def __str__(self):
        return self.email
