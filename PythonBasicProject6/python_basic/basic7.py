import urllib.request as req
from bs4 import BeautifulSoup
import requests
'''
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
<li class="common_sp_list_li">
                <div class="common_sp_thumb">
                    <a href="/recipe/6891606" class="common_sp_link">
                                                <img src="https://recipe1.ezmember.co.kr/cache/recipe/2018/06/27/bbc059c608dd01cfa43ebcb45c1882a81_m.jpg">
                    </a>
                </div>
                <div class="common_sp_caption">
                    <div class="common_sp_caption_tit line2">백종원의 부추 달걀 볶음</div>
                    <div class="common_sp_caption_rv_name" style="display: inline-block; vertical-align: bottom;">
                        <a href="/profile/recipe.html?uid=rh0301"><img src="https://recipe1.ezmember.co.kr/cache/rpf/2016/05/10/b62de48479bed7417801a49a44b9f75d1.fe6ad99758a4a3bdad870d0e08c3fe39">lee쉐프</a>
                    </div>
                    <div class="common_sp_caption_rv">
                                                    <span class="common_sp_caption_rv_star"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"><img src="https://recipe1.ezmember.co.kr/img/mobile/icon_star2_on.png"></span>
                            <span class="common_sp_caption_rv_ea">(61)</span>
                                                <span class="common_sp_caption_buyer" style="vertical-align: middle;">조회수 13.4만</span>
                    </div>
                </div>
            </li>
'''
url="https://www.10000recipe.com/recipe/list.html?order=reco&page=2"
res_html=requests.get(url)
recipe_data=res_html.text
#print(recipe_data)
soup=BeautifulSoup(recipe_data,'html.parser')
titleList=soup.select(".common_sp_caption .common_sp_caption_tit")
chefList=soup.select(".common_sp_caption_rv_name a")
imgList=soup.select(".common_sp_thumb .common_sp_link img")
hitList=soup.select(".common_sp_caption_buyer")
for i in range(0,len(titleList)):
  print(titleList[i].text)
  print(chefList[i].text)
  print(hitList[i].text)
  print("===============")








