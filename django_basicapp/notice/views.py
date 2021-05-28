from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView
from .models import Notice
# Create your views here.
'''
목록출력 => SELECT => ListView (list)
상세보기 => WHERE id=? => DetailView (detail)
추가 => INSERT => CreateView (edit)
수정 => UPDATE => UpdateView (edit)
삭제 => DELETE => DeleteView (edit)
'''
class NoticeListView(ListView):
    model = Notice

class NoticeDetailView(DetailView):
    model = Notice

class NoticeUpdateView(UpdateView):
    model = Notice
    fields = ['name','subject','content','regdate']
    template_name_suffix = '_update'
