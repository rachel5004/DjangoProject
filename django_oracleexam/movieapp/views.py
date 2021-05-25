from django.shortcuts import render
from movieapp import models
'''
  =========================================
   1. views.py : 화면에 출력할 내용 , 사용자의 입력값을 받는 경우 
   2. urls.py : 화면 이동 
   ========================================= @Controller
   3. models.py : DAO (데이터베이스 연결) 
       => 두가지 (장고에서 제공 ORM => QuerySet(sql문장을 사용하지 않고 자체에서 sql문장을 만들어 준다)
            SQL문장을 전송 
'''
# Create your views here.
def home(request):
    #page=request.GET['page'] # request.getParameter("page") , request.POST['name명']
    #print(page)
    movie_list=models.movieListData(1)
    mlist=[]
    for row in movie_list:
            print(row)
            mm={"mno":row[0],"title":row[1],"poster":row[2]}
            mlist.append(mm)
    print(mlist)
    return render(request,'movie/home.html',{"list":mlist})

def detail(request):
    movie_detail=models.movieDetailData(1)
    #mno,title,poster,genre,grade
    md={"mno":movie_detail[0],"title":movie_detail[1],"poster":movie_detail[2],"genre":movie_detail[3],"grade":movie_detail[4]}
    return render(request,'movie/detail.html',{"md":md})
def info(request):
    name='홍길동'
    return render(request,'movie/info.html',{"name":name})