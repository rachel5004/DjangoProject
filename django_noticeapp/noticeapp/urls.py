from django.urls import path
from .views import *

urlpatterns=[
    path('',NoticeList.as_view(),name='list'),
]