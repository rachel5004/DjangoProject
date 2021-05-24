from django.db import models
'''
    CREATE TABLE notice()=>ORM
    
     1. 설정 => 화면에 출력 
     1) 장고 라이브러리 로드  
        pip install django
    2) 장고의 설정 파일  (urls.py,admin.py...)
       django-admin startproject config . (현재 프로젝트에 설정하는 파일을 만든다)
    3) Web Site => DB설정 (default: sqlite3) => settings.py 
                    => DB구동 
        python manage.py migrate
    4) 관리자 모드 만들기 
       python manage.py createsuperuser 
           => id , email ,password
    4-1) 설정이 되었는지 확인 
          => 서버 구동 
          python manage.py runserver   ==> ctrl+c (서버 종료)
    5) 사용자 화면 제작 
         파일 저장의 위치 지정 
         ptthon manage.py startapp (앱이름지정) => bookmark , notice , member
     6) 모델 제작 => models.py
                          컬럼명 지정 , SQL으로 클래스 (DAO)
     7) config/settings : 앱이름 등록 
                             INSTALLED_APPS=[
                             ]
     7-1) 데이터베이스 명령이 정상수행 여부 
          python manage.py makemigrations 앱이름 
          
    7-2) 데이터베이스 적용 (models.py => Create(테이블 제작)
          python manage.py migrate
    8) admin에 모델등록 
       admin.py : => admin.site.register(앱등록)
    8-1) python manage.py runserver => http://127.0.0.1/admin => 확인 
    9) views.py => 등록 
    10) urls.py => 사이트 이동 url 등록 
         path('')   ===> notice/
         path('add/') ==> notice/add
         path('delete/') ==> notice/delete
         
         => 링크 ( <a href="{% url 'url명' pk= %}"></a>

'''
# Create your models here.
class Notice(models.Model):
    name = models.CharField(max_length=34)
    subject = models.CharField(max_length=500)
    content = models.TextField()
    regdate = models.DateTimeField()
    def __str__(self):
        return self.subject