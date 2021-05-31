from django.shortcuts import render
from django.views.generic import ListView
from .models import Noticeapp

from .models import *
# Create your views here.
class NoticeList(ListView):
    model=Noticeapp