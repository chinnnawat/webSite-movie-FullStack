from django.urls import path
from .views import logIn,register,logInUser,logout

urlpatterns=[
    path('member',logIn,name="member"),
    path('register/add',register,name="addUser"),
    path('login',logInUser,name="logInUser"),
    path('logout',logout,name='logout')
]