from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
'''
setting.py : 데이터베이스, 사용자파일(installed app) 등록
admin.py : 사이트 이름 등록
view.py : controller
model.py : 데이터베이스 연결(DAO) - 직접연결, ORM(라이브러리 이용가능)
urls.py : 사이트 등록(web.xml - *.do)
'''
# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark