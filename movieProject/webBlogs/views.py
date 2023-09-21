from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import webBlogs
from django.core.paginator import Paginator , EmptyPage , InvalidPage #แบ่งหน้า

# Create your views here.

#HomePage
def homePage(request):
    categories = Category.objects.all()
    # categories = Category.objects.filter(category_id=6)
    # webblogs = webBlogs.objects.all()

    # #Filter category
    webblogsFilter = webBlogs.objects.filter(category_id=1)

    #pagination แบ่งหน้า
    paginator = Paginator(webblogsFilter,4)
    #คลิกหน้า 1,2,3
    try:
        page = int(request.Get.get('page','1'))
    except:
        page = 1
    try:
        blockPerPage = paginator.page(page)
    except(EmptyPage,InvalidPage):
        blockPerPage = paginator.page(paginator.num_pages)
    
    return render(request,"frontEnd/homePage.html",{'categories':categories,'webblogs':blockPerPage,'webblogsFilter':webblogsFilter})

