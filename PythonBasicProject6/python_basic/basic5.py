import urllib.request as req
from bs4 import BeautifulSoup
import json
'''
   [
   {'nation': '미국', 'grade': '12세이상관람가', 'regdate': '21.03.03', 
   'genre': '드라마', 'time': '115분', 'title': '미나리', 'mno': 1}, 
   {'nation': '일본', 'grade': '15세이상관람가', 'regdate': '21.01.27', 
   'genre': '애니메이션/판타지/액션/시대극', 'time': '117분', 'title': 
   '극장판 귀멸의 칼날: 무한열차편', 'mno': 2}, 
   {'nation': '미국', 'grade': '전체관람가', 'regdate': '21.03.04', 
   'genre': '애니메이션/어드벤처/코미디', 'time': '114분', 
   'title': '라야와 마지막 드래곤', 'mno': 3}, 
   {'nation': '뉴질랜드, 미국', 'grade': '12세이상관람가', 'regdate': '21.03.11', 'genre': '판타지/어드벤처', 'time': '165분 , 181분(재개봉)', 'title': '반지의 제왕 : 반지 원정대', 'mno': 4}, {'nation': '미국', 'grade': '15세이상관람가', 'regdate': '21.03.11', 'genre': '액션', 'time': '100분', 'title': '리스타트', 'mno': 5}, {'nation': '스페인', 'grade': '15세이상관람가', 'regdate': '21.03.11', 'genre': '액션/어드벤처/범죄', 'time': '118분', 'title': '웨이 다운', 'mno': 6}, {'nation': '미국', 'grade': '전체관람가', 'regdate': '21.01.20', 'genre': '애니메이션/판타지', 'time': '107분', 'title': '소울', 'mno': 7}, {'nation': '미국, 뉴질랜드, 독일', 'grade': '12세이상관람가', 'regdate': '21.03.18', 'genre': '액션/어드벤처/판타지', 'time': '177분', 'title': '반지의 제왕 : 두 개의 탑', 'mno': 8}, {'nation': '미국, 뉴질랜드, 독일', 'grade': '12세이상관람가', 'regdate': '21.03.18', 'genre': '액션/어드벤처/판타지', 'time': '199분', 'title': '반지의 제왕 : 왕의 귀환', 'mno': 9}, {'nation': '홍콩', 'grade': '15세이상관람가', 'regdate': '21.03.04', 'genre': '드라마', 'time': '102분 , 103분(재개봉)', 'title': '중경삼림', 'mno': 10}]

'''
class MovieSystem:
    def movie_list(self):
        #웹서버 연결
        page=int(input("페이지 입력:"))
        url=f"http://127.0.0.1/web/movie/list.do?page={page}"
        web_data=req.urlopen(url).read().decode('utf-8')
        #데이터 출력 
        print(web_data)
        #json으로 변경 
        json_data=json.loads(web_data)
        print(json_data)
        #데이터만 추출 
        for movie in json_data:
            print("===============================")
            print("영화제목:"+movie['title'])
            print("상영일:"+movie['regdate'])
            print("장르:"+movie['genre'])
            print("등급:"+movie['grade'])
            print("제작국:"+movie['nation'])
            print("상영시간:"+movie['time'])
            print(f"순위:{movie['mno']}")
            # "순위:%d" %movie['mno']   %(값,값...) []=list=List {"":""}=딕트=Map
    
    def movie_detail(self,mno):
        url="http://127.0.0.1/web/movie/detail.do?mno="+str(mno)
        web_data=req.urlopen(url).read().decode('utf-8')
        print(web_data)
        movie=json.loads(web_data)
        print(movie)
        
        print("===============================")
        print("영화제목:"+movie['title'])
        print("상영일:"+movie['regdate'])
        print("장르:"+movie['genre'])
        print("등급:"+movie['grade'])
        print("제작국:"+movie['nation'])
        print("상영시간:"+movie['time'])
        print(f"순위:{movie['mno']}")
        print("박스오피스:"+movie['boxoffice'])
        print("누적관객:"+movie['showuser'])
        print(f"평점:{movie['score']}")
        print("줄거리:"+movie['story'])
        

#mno=int(input("상세볼 영화 번호:"))
#movie_detail(mno)   
movie=MovieSystem()
#movie.movie_list()
mno=int(input("상세볼 영화 번호:"))
movie.movie_detail(mno)
   
    
    
    
    
    
    
    
    