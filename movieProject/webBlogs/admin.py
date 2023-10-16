from django.contrib import admin
from .models import webBlogs,Comment,ReviewRating

#ให้ Admin จัดการ app webBlogs
admin.site.register(webBlogs)
admin.site.register(Comment)
admin.site.register(ReviewRating)