from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        #로그인 정보가 맞는지 확인
        user = authenticate(username=username, password=password)
        if user is not None:
            print("sucess")
            login(request, user)
        else:
            print("failed")

    return render(request, "users/login.html")