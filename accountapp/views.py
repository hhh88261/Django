from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

# Create your views here.

def myblog(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            print("로그인 성공")
            login(request, user)
            return redirect('accountapp:myblog')
        else:
            print("로그인 실패")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('accountapp:myblog')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('accountapp:login')

    return render(request, 'signup.html')

