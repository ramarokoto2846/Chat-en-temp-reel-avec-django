from django.contrib import admin
from .models import CustomUser, Messages

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Messages)