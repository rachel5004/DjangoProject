from django.urls import path
from siteapp import views
urlpatterns=[
    path('',views.index),  # http://127.0.0.1:8000/site
    path('board/',views.board) #http://127.0.0.1:8000/site/board
]