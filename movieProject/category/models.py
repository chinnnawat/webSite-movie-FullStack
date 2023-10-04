from django.db import models

# Create your models here.
# Create ตัวแปรที่กำหนดใน MS Word
# name ประเภทหนัง
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True) #unique => True => ห้ามตั้งชื่อประเภทหนังซ้ำกัน 
    
    def __str__(self):
        return self.name