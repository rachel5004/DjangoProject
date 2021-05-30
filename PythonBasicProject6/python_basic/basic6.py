import urllib.request as req
from bs4 import BeautifulSoup
import requests
'''
 <td class="title">
                        <div class="tit3">
                            <a href="/movie/bi/mi/basic.nhn?code=189150" title="분노의 질주: 더 얼티메이트">분노의 질주: 더 얼티메이트</a>
                        </div>
                    </td>
'''
url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
movie_data=requests.get(url)
movie_data=movie_data.text
#print(movie_data)
soup=BeautifulSoup(movie_data,'html.parser')
mList=soup.select(".title > .tit3 > a")
for movie_title in mList:
    print(movie_title.attrs['href'])
    print(movie_title.text)