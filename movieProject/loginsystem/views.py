from django.shortcuts import render

# Create your views here.
def logIn(request):
    return render(request,"frontEnd/login.html")
