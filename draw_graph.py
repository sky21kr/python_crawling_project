import matplotlib.pyplot as plt
import datetime
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def calc_avg(lst,y): #리스트의 영화들의 총 합을 y리스트에 추가
    s = 0
    for movie in lst:
        s = s + int(movie[1])
        
    if len(lst) == 0:
        y.append(s)
    else:
        y.append(s/len(lst))
    print(s)
    
file = open("movies_info.txt","r")

Top_Movie = [] # 천만 관객 영화 리스트
All_Movie = [] # 모든 영화 리스트
    
for key in file: # 파일 읽어와서 []
    lst = key.split('|')
    lst[2] = lst[2].replace('\n', '')
    
    if( lst[2] != ' '):
        All_Movie.append(lst) # 모든 영화들 리스트에 저장
        
        if( int(lst[1]) >= 10000000):# 영화 관객수가 1000만 이상이면 Top_Movie 리스트에도 저장
            Top_Movie.append(lst)

s = 0
for movie in All_Movie: # 모든 영화의 관객수의 합 저장
    s = s + int(movie[1])

x = ['2주 전','1주 전', '같은 주', '1주 뒤', '2주 뒤'] # 그래프의 x축

for T_Movie in Top_Movie: # 1000만 이상 영화의 각각을 조사
    now_date = datetime.datetime.strptime(T_Movie[2].replace('-',''),'%Y%m%d')
    r = now_date.weekday()
    
    M_date = now_date + datetime.timedelta(days=-1*r) # M_date는 영화 개봉한 주의 월요일의 날짜
    B2_date = M_date + datetime.timedelta(days=-14) # 2주 전 월요일
    B1_date = M_date + datetime.timedelta(days=-7) # 1주 전 월요일
    A1_date = M_date + datetime.timedelta(days=7) # 1주 뒤 월요일
    A2_date = M_date + datetime.timedelta(days=14) # 2주 뒤 월요일
    A3_date = M_date + datetime.timedelta(days=21) # 3주 뒤 월요일
    print("{}:{}".format("천만영화",T_Movie))

    y = [] # 그래프의 y축
    B2 = [] # 2주 전 주의 영화 리스트
    B1 = [] # 1주 전 주의 영화 리스트
    S = []  # 같은 주 의 영화 리스트
    A1 = [] # 1주 후 주의 영화 리스트
    A2 = [] # 2주 후 주의 영화 리스트
    
    for A_Movie in All_Movie:
        date = datetime.datetime.strptime(A_Movie[2].replace('-',''),'%Y%m%d')
        if( B2_date <= date < B1_date ): #2주 전과 같은 주
            B2.append(A_Movie)
        elif( B1_date <= date < M_date): #1주 전과 같은 주
            B1.append(A_Movie)
        elif( M_date <= date < A1_date and A_Movie[0] != T_Movie[0]): #같은 주
            S.append(A_Movie)
        elif( A1_date <= date < A2_date ): #1주 뒤와 같은 주
            A1.append(A_Movie)
        elif( A2_date <= date < A3_date): #2주 뒤와 같은 주
            A2.append(A_Movie)

    
    calc_avg(B2,y) # 2주 전 영화 리스트 평균 관객 수 계산
    calc_avg(B1,y) # 1주 전 영화 리스트 평균 관객 수 계산
    calc_avg(S,y)  # 같은 주 영화 리스트 평균 관객 수 계산
    calc_avg(A1,y) # 1주 뒤 영화 리스트 평균 관객 수 계산
    calc_avg(A2,y) # 2주 뒤 영화 리스트 평균 관객 수 계산

    # matplotlib.pyplot를 이용한 그래프 그리기
    plt.plot(x,y)
    plt.axhline(y = s / len(All_Movie), color = 'r', linewidth=1) # 전체 영화 평균 보조선
    plt.xlabel('date')
    plt.ylabel('number')
    plt.title(T_Movie[0])

    plt.show()

file.close()
