import json
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
proxies = { "http": "http://114.239.150.199", } 
url="https://pvp.qq.com/web201605/js/herolist.json"
r=requests.get(url,headers=headers,proxies=proxies,stream=True)
hero_list = json.loads(r.text)
pd.set_option('display.width', 200)
hero_list = None
#保存
with open("allheros.json", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
#恢复
with open('allheros.json','rb') as json_data:
    hero_list = json.load(json_data)
    
hero_type =["全部","战士","法师","坦克","刺客","射手","辅助"]
all_heros=[]
for hero in hero_list:
    hero_des=[hero['cname'],build_hero_type(hero),hero['skin_name'].strip("&#10;'")]
    all_heros.append(hero_des)
all_des=pd.DataFrame(all_heros,columns=['name', 'type',"skin"])

browser = webdriver.Chrome('./chromedriver')
browser.get("https://pvp.qq.com/web201605/herolist.shtml")
html = browser.page_source
browser.quit()
#保存
with open("hero_web.html", 'w',encoding="utf-8") as fd:
     fd.write(html)
## 恢复保存的HTML
hero_html = None
with open("hero_web.html", 'r',encoding="utf-8") as fd:
     hero_html = fd.read()
hero_soup = bs(html,'lxml')
hero_detail=hero_soup.find("ul",class_="herolist clearfix")
all_hero_detail=hero_detail.find_all("li")
hero_details=[]
for i in all_hero_detail:
    hero_detail=[i.text,"http:"+i.img["src"]]
    hero_details.append(hero_detail)
hero_track=pd.DataFrame(hero_details,columns=['name','skin_link'])
#combine=pd.merge(all_des,hero_track,on=['name'],how="left")
def build_hero_type(hero):
    combine_type = []    
    if "hero_type" in hero:
        combine_type.append(hero_type[hero["hero_type"]])
    if "new_type" in hero:
        combine_type.append(hero_type[hero["new_type"]])
    if "hero_type2" in hero:
        combine_type.append(hero_type[hero["hero_type2"]])
    return(('|').join(combine_type))
def get_hero_info(hero):
    combine=pd.merge(all_des,hero_track,on=['name'],how="left")
    hero=combine[combine['name'].isin(["廉颇"])]
    print(hero)
def serch_hero(hero):
    start=time.time()
    get_hero_info(hero)
    end=time.time()
    print('Running time:''{}'.format(end-start))

——————————————————————————————————
fenci
import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
from PIL import Image
import jieba
a=str(all_heros)
b=a.replace("|","",1000)
fen=jieba.cut(b,cut_all=False)
space=" ".join(fen)
keywords = jieba.analyse.extract_tags(b, topK=300, withWeight=True, allowPOS=())
keywords
wc = WordCloud(
    #width=800,
    #height=600,
    background_color="white",  # 设置背景颜色
#    max_words=200,  # 词的最大数（默认为200）
    colormap='viridis',  # string or matplotlib colormap, default="viridis"
    random_state=10,  # 设置有多少种随机生成状态，即有多少种配色方案
    font_path='./fonts/cn/msyh.ttc',
    stopwords=('全部','法师','坦克','刺客','辅助','射手','战士')
)
##comments
my_wordcloud = wc.generate(space)
import matplotlib.pyplot as plt
%matplotlib inline

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
