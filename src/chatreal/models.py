from django.contrib.auth.models import AbstractUser
from django.db import models
import random

# Create your models here.
class CustomUser(AbstractUser):
    uid = models.CharField(
        max_length=10,
        editable=False,
        unique=True
    )
    username = models.CharField(max_length=15, unique=True, verbose_name="Pseudo")
    email = models.EmailField(unique=True, verbose_name="Adresse e-mail")
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True, verbose_name="Photo de profil")

    def __str__(self):
        return f"Pseudo: {self.username}, uid: {self.uid}"

    def save(self, *args, **kwargs):
        if not self.uid:
            uid = []
            re = ''
            for i in range(10):
                a = random.randint(0, 9)
                uid.append(a)

            for e in uid:
                e_str = str(e)
                re = re + e_str
            self.uid = re
        super().save(*args, **kwargs)


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.permission',
        related_name='customuser_permissions',
        blank=True
    )