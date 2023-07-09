from django.contrib import admin
from .models import User, board

# Register your models here.

admin.site.register(User)

class Board(admin.ModelAdmin):
    list_display = ['username','title']
    list_display_link = ['username', 'title']
