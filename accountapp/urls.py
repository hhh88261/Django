from django.urls import path
from . import views
from accountapp.views import myblog,login_view,logout_view

app_name = "accountapp"

urlpatterns = [
    path('',myblog, name='myblog'),
    path("login",views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),
    path("signup",views.signup, name='signup'),
]