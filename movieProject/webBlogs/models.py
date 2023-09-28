from django.db import models
from category.models import Category #inport from app category

# Create your models here.
class webBlogs(models.Model):
    name = models.CharField(max_length=255) #Move's name
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)     #วิธีเชื่อมจากไฟล์นอก
    writer = models.CharField(max_length=255)   #user's name comment
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="blogImage",blank=True)
    created = models.DateTimeField(auto_now_add=True)   #Date upload movie
    link = models.CharField(max_length=2000, default='ไม่มี URL')
    linkTeaser = models.CharField(max_length=2000, default='ไม่มี URL')
    likes = models.IntegerField(default=0)

    #นำไปแสดงผล
    def __str__(self):
        return self.name


