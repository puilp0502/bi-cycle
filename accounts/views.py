from django.shortcuts import render, redirect
from django.contrib.auth import logout as _logout

from .models import User

def signup(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        area = request.POST['area']
        useradd = User(username=username,
                       password=password,
                       name=name,
                       email=email,
                       phone_number=phone_number,
                       area=area)
        useradd.set_password(password)
        useradd.save()
    return redirect('accounts:login')


def logout(request):
    _logout(request)
    return redirect('/')
