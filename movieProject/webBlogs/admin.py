from django.contrib import admin
from .models import webBlogs
# Register your models here.

#ให้ Admin จัดการ app webBlogs
admin.site.register(webBlogs)