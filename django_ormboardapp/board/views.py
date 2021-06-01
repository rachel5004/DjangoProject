from django.db.models import F
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Board
from django.urls import reverse_lazy
# Create your views here.
class BoardListView(ListView):
      model=Board
      paginate_by = 5 #rowSize=5

class BoardCreateView(CreateView):
      model=Board
      fields=['name','subject','content','pwd']  # insert into board(name,subject,content,pwd)
      success_url = reverse_lazy('list')
      template_name_suffix = '_create'
class BoardDetailView(DetailView):
      model=Board

class BoardUpdateView(UpdateView):
      model= Board
      fields=['name','subject','content']
      template_name_suffix = "_update"
class BoardDeleteView(DeleteView):
      model=Board
      success_url = reverse_lazy('list')







