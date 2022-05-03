import requests
from bs4 import BeautifulSoup as bs

def crawling():

    word_list={}
    word_name = []
    word_meaning = []

    url = "https://terms.naver.com/list.naver?cid=42088&categoryId=42088"


    data_page = requests.get(url)
    soup = bs(data_page.content,"html.parser")

    result = soup.select("#content div.list_wrap>ul>li>div.info_area>div.subject>strong>a")
    result2 = soup.select("#content div.list_wrap>ul>li>div.info_area>p")

    for i in range(0,len(result)):
        if i%2==0:
            word_name.append(result[i].get_text())
    for i in result2:
        word_meaning.append(i.get_text().strip())
        
    list_meaning=[] #설명이 길어서 가장 앞 부분의 설명만 담기

    for i in range(0,len(word_meaning)):
        list_meaning.append((word_meaning[i].split('.')[0]))

    word_list['name'] = word_name
    word_list['meaning'] = list_meaning
    return word_list

datas = crawling()
print(len(datas['name']))