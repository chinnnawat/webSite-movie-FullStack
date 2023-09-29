from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import webBlogs
from django.core.paginator import Paginator , EmptyPage , InvalidPage #แบ่งหน้า

# Create your views here.

#HomePage
def homePage(request):
    #Action = 1
    categories = Category.objects.all()
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

    
    
    return render(request,"frontEnd/homePage.html",{'categories':categories,'webblogs1':blockPerPage1,'webblogsFilter1':webblogsFilter1,'webblogs6':blockPerPage6,'webblogs2':blockPerPage2,'popular':popular,'suggest':suggest})

def showPlayer(request,id):
    categories = Category.objects.all()
    
    singleMovie = webBlogs.objects.get(id=id)
    singleMovie.views = singleMovie.views+1
    singleMovie.save()

    #Suggestion Movie
    suggest = webBlogs.objects.all().order_by('views')[:4] #min->max 3 movies
    return render(request,"frontEnd/showPlay.html",{"singleMovie":singleMovie,'categories':categories,'suggest':suggest})

#search category
def searchCategory(request,cat_id):
    movieList = webBlogs.objects.filter(category_id=cat_id)

    categories = Category.objects.all()
    return render(request,"frontEnd/list.html",{'movieList':movieList,'categories':categories})
