from django.contrib import admin
from .models import Category

# Register your models here.

#ให้ Admin จัดการ app category
admin.site.register(Category)