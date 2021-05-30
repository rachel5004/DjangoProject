# http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
from bs4 import BeautifulSoup
import requests
import sqlite3
url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data=requests.get(url)
xml=data.text
# Document doc=Jsoup.connect(url).get()
#print(xml)
'''
   <location wl_ver="3">
    <province>서울ㆍ인천ㆍ경기도</province>
    <city>서울</city>
    <data>
    <mode>A02</mode>
    <tmEf>2021-05-24 00:00</tmEf>
    <wf>구름많음</wf>
    <tmn>17</tmn>
    <tmx>25</tmx>
    <reliability/>
    <rnSt>20</rnSt>
    </data>
'''

conn=sqlite3.connect("weather.db")
'''
cursor=conn.cursor()
sql="DROP TABLE IF EXISTS weather"
cursor.execute(sql)
cursor.close()
print("테이블 삭제 완료")
cursor=conn.cursor()
sql="""
     CREATE TABLE IF NOT EXISTS weather( 
        city text,
        mode text,
        wf text,
        tmn integer,
        tmx integer
     )
    """
cursor.execute(sql)
cursor.close()
conn.close()
print("날씨 데이터베이스 생성")
'''
'''
soup=BeautifulSoup(xml,'html.parser')
for location in soup.find_all('location'):
    #print(location)
  try:
    city=location.find("city").string
    #print(city)
    mode=location.find("mode").string
    #tmEf=location.find("tmEf").string
    wf=location.find("wf").string
    tmn=location.find("tmn").string
    tmx=location.find("tmx").string
    #rnSt=location.find("rnSt")
    print(city,mode,wf,tmn,tmx)
    #데이터베이스에 첨부 
    cursor=conn.cursor()
    sql="""
         INSERT INTO weather VALUES(?,?,?,?,?)
        """
    cursor.execute(sql,(city,mode,wf,tmn,tmx))
    print("데이터 첨부 완료")
    conn.commit()
    cursor.close()
  except Exception as e:
      pass
'''
city=input("지역 입력:")
cursor=conn.cursor()
sql=f"SELECT * FROM weather WHERE city='{city}'"
cursor.execute(sql)
data=cursor.fetchone()
print("지역:"+data[0])
print("날씨:"+data[2])
print("온도:"+str(data[3])+"/"+str(data[4]))
cursor.close()







