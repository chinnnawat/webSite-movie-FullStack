from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#HomePage
def homePage(request):
    return render(request,"frontEnd/homePage.html")
