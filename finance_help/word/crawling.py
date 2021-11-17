import requests
from bs4 import BeautifulSoup as bs

word_list={}
word_name = []
word_meaning = []

#시도 1
#https://fine.fss.or.kr/main/fin_tip/dic/financedic.jsp => 연결거부
# soup1=soup.select_one("#container section.fixed_width>div.table_area>ul.dic_result_list>li")
# print(soup1)

#시도 2
# url = "https://terms.naver.com/list.naver?searchId=pv322" => 데이터별로이고 용어와 관련된 것은 2개밖에 없음 아웃.
#//*[@id="content"]/div[4]/ul/li[1]/div[2]/div[1]/strong/a[1]
#//*[@id="content"]/div[4]/ul/li[1]/div[2]/p
# result = soup.select("#content div.list_wrap>ul>li>div.info_area>div.subject>strong>a")
# result2 = soup.select("#content div.list_wrap>ul>li>div.info_area>p")

url = "https://terms.naver.com/list.naver?cid=42088&categoryId=42088"


data_page = requests.get(url)
soup = bs(data_page.content,"html.parser")

#//*[@id="content"]/div[4]/ul/li[1]/div/div[1]/strong/a[1]

result = soup.select("#content div.list_wrap>ul>li>div.info_area>div.subject>strong>a")
result2 = soup.select("#content div.list_wrap>ul>li>div.info_area>p")
for i in range(0,len(result)):
    if i%2==0:
        word_name.append(result[i].get_text())
for i in result2:
    word_meaning.append(i.get_text().strip())
    

# print(word_name)
#print(word_meaning)


list_meaning=[]
# print(word_meaning[0])
# print((word_meaning[0].split('.')[0]))

for i in range(0,len(word_meaning)):
    #print(word_meaning[i].split('.')[0])
    list_meaning.append((word_meaning[i].split('.')[0]))

# print(list_meaning)


import pandas as pd
df = pd.DataFrame()
#print(df)
df['name'] = pd.DataFrame(word_name)
df['meaning'] = pd.DataFrame(list_meaning)
print(df)