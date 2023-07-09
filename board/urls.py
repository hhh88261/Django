from django.urls import path
from . import views
from board.views import board_list, gallery

app_name = "board"

urlpatterns = [
    path("board",views.board_list, name='board'),
    path('gallery',views.gallery, name='gallery'),
]