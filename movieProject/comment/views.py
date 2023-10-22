from django.shortcuts import render,redirect
from webBlogs.models import Comment
from category.models import Category
from webBlogs.models import webBlogs
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def panel(request):
    return render(request,"frontEnd/comment.html")

@login_required(login_url="member")
# Create your views here.
def showPlayer(request,id):
    categories = Category.objects.all()
    singleMovie = webBlogs.objects.get(id=id)
    singleMovie.views = singleMovie.views+1
    singleMovie.save()

    #Suggestion Movie
    suggest = webBlogs.objects.all().order_by('views')[:3] #min->max 3 movies
    return render(request,"frontEnd/showPlay.html",{"singleMovie":singleMovie,'categories':categories,'suggest':suggest})

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

def insertData(request):
    if request.method == "POST":
        comment = request.POST["comment"]
        writer = auth.get_user(request)
        comment = Comment(body = comment,name = writer)
        comment.save()
        messages.info(request,"completed")
        return redirect("homePage")
    else:
        messages.info(request,"cancel")
        return redirect("homePage")