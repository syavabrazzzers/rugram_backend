from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from donuts.models import Donut
from sweetusers.models import User
# Register your models here.

admin.site.register(Donut)
admin.site.register(User, UserAdmin)