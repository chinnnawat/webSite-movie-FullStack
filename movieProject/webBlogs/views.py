from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import webBlogs
from django.core.paginator import Paginator , EmptyPage , InvalidPage #แบ่งหน้า
from django.http import JsonResponse

def homePage(request):
    #Action = 1
    categories = Category.objects.all()
    loopCategory = webBlogs.objects.all()
    webblogsFilter1 = webBlogs.objects.filter(category_id=1)
    paginator1 = Paginator(webblogsFilter1,4)

    try:
        page = int(request.Get.get('page','1'))
    except:
        page = 1
    try:
        blockPerPage1 = paginator1.page(page)
    except(EmptyPage,InvalidPage):
        blockPerPage1 = paginator1.page(paginator1.num_pages)
    
    #Anime = 6
    webblogsFilter6 = webBlogs.objects.filter(category_id=6)
    paginator6 = Paginator(webblogsFilter6,4)

    try:
        page = int(request.Get.get('page','1'))
    except:
        page = 1
    try:
        blockPerPage6 = paginator6.page(page)
    except(EmptyPage,InvalidPage):
        blockPerPage6 = paginator6.page(paginator6.num_pages)

    # Drama
    webblogsFilter2 = webBlogs.objects.filter(category_id=2)
    paginator2 = Paginator(webblogsFilter2,4)

    try:
        page = int(request.Get.get('page','1'))
    except:
        page = 1
    try:
        blockPerPage2 = paginator2.page(page)
    except(EmptyPage,InvalidPage):
        blockPerPage2 = paginator2.page(paginator2.num_pages)

    #PopularMovie
    popular = webBlogs.objects.all().order_by('-views')[:3] #max->min 3 movies

    #Suggestion Movie
    suggest = webBlogs.objects.all().order_by('views')[:3] #min->max 3 movies

    
    
    return render(request,"frontEnd/homePage.html",{'categories':categories,'webblogs1':blockPerPage1,'webblogsFilter1':webblogsFilter1,'webblogs6':blockPerPage6,'webblogs2':blockPerPage2,'popular':popular,'suggest':suggest,'loopCategory':loopCategory})

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
    return render(request, "frontEnd/homePage.html", {'movieList': pagePerwebblog, 'categories': categories})

#search bar
def search(request):
    categories = Category.objects.all()
    if request.method =="POST":
        searched = request.POST['searched']
        venue = webBlogs.objects.filter(name__icontains = searched)
        return render(request,"frontEnd/search.html",{'searched':searched,'venue':venue,'categories':categories})
    else:
        return render(request,"frontEnd/search.html",{'searched':searched,'categories':categories})

