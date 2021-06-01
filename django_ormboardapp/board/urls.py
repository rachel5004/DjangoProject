from django.urls import path,include
from .views import BoardListView,BoardCreateView,BoardDetailView,BoardUpdateView,BoardDeleteView
# Spring => @RequestMapping()
urlpatterns=[
    path('',BoardListView.as_view(),name="list"),
    #@RequestMapping("board/insert.do")
    path('insert/',BoardCreateView.as_view(),name="insert"),
    path('detail/<int:pk>',BoardDetailView.as_view(),name='detail'),
    path('update/<int:pk>',BoardUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',BoardDeleteView.as_view(),name='delete')
]