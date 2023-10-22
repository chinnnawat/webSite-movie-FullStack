from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from webBlogs.models import ReviewRating, webBlogs
from django.core.paginator import Paginator , EmptyPage , InvalidPage #แบ่งหน้า
from django.contrib.auth.decorators import login_required
from django.contrib import auth

@login_required(login_url="member")
# Create your views here.
def showPlayer(request,id):
    categories = Category.objects.all()
    singleMovie = webBlogs.objects.get(id=id)
    singleMovie.views = singleMovie.views+1
    singleMovie.save()

    

    #Suggestion Movie
    suggest = webBlogs.objects.all().order_by('views')[:3] #min->max 3 movies

    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id = singleMovie.id, status = True)
    context = {
        'singleMovie':singleMovie,
        'categories':categories,
        'suggest':suggest,
        'reviews':reviews,
    }
    return render(request,'frontEnd/showPlay.html',context)

#search category
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def searchCategory(request, cat_id):
    movieList = webBlogs.objects.filter(category_id=cat_id)

    # pagination
    paginator = Paginator(movieList, 12)  # สร้าง Paginator จาก movieList และกำหนดให้แสดง 3 รายการต่อหน้า

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        pagePerwebblog = paginator.page(page)  # ดึงหน้าที่ร้องขอ
    except (EmptyPage, InvalidPage):
        pagePerwebblog = paginator.page(paginator.num_pages)  # หากหน้าไม่มีอยู่ให้ใช้หน้าสุดท้าย

    # category
    categories = Category.objects.all()
    return render(request, "frontEnd/list.html", {'movieList': pagePerwebblog, 'categories': categories})
