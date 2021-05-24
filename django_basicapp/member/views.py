from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Member
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
# Create your views here.
class MemberListView(ListView):
    model = Member

class MemberCreateView(CreateView):
    model = Member
    fields = ['name','sex','addr','tel']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class MemberDetailView(DetailView):
    model = Member

class MemberUpdateView(UpdateView):
    model = Member
    fields = ['name', 'sex', 'addr', 'tel']
    template_name_suffix = '_update'

class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('list')
