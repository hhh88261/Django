from django import forms
from .models import Board
from django_summernote.field import SummernoteTextfield
from django_summernote.widgets import SummernoteWidget

class BoardWirtenForm(forms.modelsForm):

