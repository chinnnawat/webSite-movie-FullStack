from django.db import models
from category.models import Category #inport from app category
from django.db.models import Avg,Count

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
    
    def averageReview(self):
        reviews = ReviewRating.objects.filter(product = self, status = True).aggregate(average = Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def countReview(self):
        reviews = ReviewRating.objects.filter(product = self, status = True).aggregate(count = Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
    
class Comment(models.Model):
    post = models.ForeignKey(webBlogs,related_name="comments",on_delete=models.CASCADE)
    userName = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def  __str__(self):
        return '%s - %s' % (self.post.name, self.userName)
        # return self.name

class ReviewRating(models.Model):
    product = models.ForeignKey(webBlogs,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,blank=True)
    review = models.TextField(max_length=500,blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20,blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def  __str__(self):
        return self.subject
        # return self.name

