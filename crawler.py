import urllib
import datetime
from bs4 import BeautifulSoup
import requests

key = "6ac9c871833f14d5d1fb863406a7d600" # 할당받은 키 값
default_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml?key="

date = datetime.datetime.strptime('20191110','%Y%m%d')
dic = {} # 데이터를 담기 위한 딕셔너리
dic_value = [] # 값을 담기 위한 배열

f = open('movies_info_.txt', 'w')
k = 0

while(1):
    date = date + datetime.timedelta(days=-7) # 11월 3일부터 시작
    str_date = str(date)[0:10].replace('-','')
    print(str_date)
    
    url = default_url + key + "&weekGb=0" + "&targetDt=" + str_date
    req = requests.get(url)
    html = req.text
    
    soup = BeautifulSoup(html, 'html.parser')
    moviename = soup.find_all('movienm') # 영화 제목
    audnum = soup.find_all('audiacc') # 누적 관객수
    openday = soup.find_all('opendt') # 개봉 날짜

    # 딕셔너리에 키 값은 영화 제목으로, 값은 누적 관객수, 개봉 일자를 리스트에 담에 저장
    for i in range(len(moviename)):
        if moviename[i].text not in dic:
            dic_value = []
            dic_value.append(audnum[i].text)
            dic_value.append(openday[i].text)
            dic[moviename[i].text] = dic_value

    if (int(str_date) <= 20040101): #
        for movie in dic: # { 영화 제목 : 누적 관객수, 개봉 일자 } 형태의 딕셔너리
            f.write(movie + '|' + dic[movie][0] + '|' + dic[movie][1] + '\n') 
        f.close()
        break

