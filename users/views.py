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
    
def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):

    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect("user:login")

    return render(request, "users/signup.html")    
