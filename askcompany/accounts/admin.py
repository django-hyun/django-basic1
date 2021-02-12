from django.contrib import admin
from .models import User
from accounts.models import Profile


# Register your models here.
@admin.register (User)
class UserAdmin (admin.ModelAdmin):
    list_display = ['id', 'email']


@admin.register(Profile)
class ProfileaAdmin(admin.ModelAdmin):
   pass

