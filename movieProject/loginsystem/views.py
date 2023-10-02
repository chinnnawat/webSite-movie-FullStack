from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.
def logIn(request):
    return render(request,"frontEnd/login.html")


# Register
def register(request):
    #check method = post ?
    if request.method =="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        #check Void
        if username == "" or email == "" or password == "" or repassword == "":
            messages.info(request,"Please enter complete information.")
            return redirect('member')
        else:
            if password == repassword :
                #check same username
                if User.objects.filter(username=username).exists():
                    messages.info(request,"cannot use this username")
                    return redirect('member')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"cannot use this email")
                    return redirect('member')
                else:
                    #create user
                    user = User.objects.create_user(
                        username = username,
                        email = email,
                        password = password
                    )
                    user.save()
                    messages.info(request,"Completed Account")
                    return redirect('member')
            else :
                messages.info(request,"not correct")
                return redirect('member')
        
# LogIn
def logInUser(request):
    username = request.POST["username"]
    password = request.POST["password"]

    #check username and password with data base
    user = auth.authenticate(username=username,password=password)
    #found ?
    if user is not None:
        auth.login(request,user)
        return redirect("homePage")
    else:
        messages.info(request,"please create new account")
        return redirect("member")
    
#LogOut
def logout(request):
    auth.logout(request)
    return redirect("homePage")

