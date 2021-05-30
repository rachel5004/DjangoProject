#-*- coding:utf-8 -*-
import urllib.request as req
from bs4 import BeautifulSoup
from urllib import parse
import json
'''
   {
      'startYearDate': '2021.05.20', 
      'endYearDate': '2021.05.20', 
      'startDate': '2021년 05월 20일(목)', 
      'endDate': '2021년 05월 20일(목)', 
      'movieCd': '20205041', 
      'showDt': '20210520', 
      'thumbUrl': '/common/mast/movie/2021/04/thumb/thn_9520edbd1421425b8ca2fac6ebddf127.jpg', 
      'movieNm': '분노의 질주: 더 얼티메이트', 
      'movieNmEn': 'Fast & Furious 9 THE FAST SAGA', 
      'synop': '기다림은 끝났다!\r\n전 세계가 기다려온 단 하나의 액션블록버스터!\r\n\r\n도미닉(빈 디젤)은 자신과 가장 가까웠던 형제 제이콥(존 시나)이 사이퍼(샤를리즈 테론)와 연합해\r\n전 세계를 위기로 빠트릴 위험천만한 계획을 세운다는 사실을 알게 되고,\r\n이를 막기 위해 다시 한번 패밀리들을 소환한다.\r\n\r\n가장 가까운 자가 한순간, 가장 위험한 적이 된 상황\r\n도미닉과 패밀리들은 이에 반격할 놀라운 컴백과 작전을 세우고\r\n지상도, 상공도, 국경도 경계가 없는 불가능한 대결이 시작되는데...', 
      'prdtYear': '2021', 
      'indieYn': None, 
      'artmovieYn': None, 
      'multmovieYn': None, 
      'showTm': '142', 
      'showTs': '40', 
      'director': '저스틴 린', 
      'prNm': None, 
      'dtNm': '유니버설픽쳐스인터내셔널 코리아(유)', 
      'repNationCd': '미국', 
      'movieType': '장편', 
      'moviePrdtStat': '개봉', 
      'genre': '액션', '
      watchGradeNm': '12세이상관람가', 
      'openDt': '20210519', 
      'salesAmt': 973715470, 
      'audiCnt': 104097, 'scrCnt': 2099, 
      'showCnt': 7293, 
      'rank': 1, 'rankInten': 0, 
      'rankOldAndNew': 'OLD', 
      'rownum': 1}
      
      searchMainDailyBoxOffice.do
      searchMainRealTicket.do
      searchMainDailySeatTicket.do
      searchMainOnlineDailyBoxOffice.do

'''
selnum=int(input("1.박스오피스,2.실시간 예매율,3.좌석점유율,4.온라인 상영관 :"))
url=''
if selnum==1:
    print("박스오피스")
    url="https://www.kobis.or.kr/kobis/business/main/searchMainDailyBoxOffice.do"
elif selnum==2:
    print("실시간 예매율")
    url="https://www.kobis.or.kr/kobis/business/main/searchMainRealTicket.do"
elif selnum==3:
    print("좌석점유율")
    url="https://www.kobis.or.kr/kobis/business/main/searchMainDailySeatTicket.do"
elif selnum==4:
    print("온라인 상영관")
    url="https://www.kobis.or.kr/kobis/business/main/searchMainOnlineDailyBoxOffice.do"

web_data=req.urlopen(url).read().decode('utf-8')
print(web_data)
json_data=json.loads(web_data)
print(json_data)

for movie in json_data:
    print("영화명:"+movie['movieNm'])
    print("감독:"+movie['director'])
    print("장르:"+movie['genre'])
    print("등급:"+movie['watchGradeNm'])
    print("상영시간:"+movie['showTm'])
    print(movie['thumbUrl'])
    print("=============================")
    
    
    
    
    
    
    
    
    
    