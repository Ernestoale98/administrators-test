from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="users/pictures",
        height_field=None,
        blank=True,
        null=True
    )
    rol = models.ForeignKey(
        'Rol',
        on_delete=models.CASCADE,
    )
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Rol(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
