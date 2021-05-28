from django.urls import path
from foodapp import views

urlpatterns=[
    path('',views.category),
    path('list/',views.foodList),
    path('detail/',views.foodDetail)
]