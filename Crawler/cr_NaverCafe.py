import urllib.request
import ssl
import datetime
import os
import pandas as pd
import time
import random

from bs4 import BeautifulSoup       # Beautiful Soup 설치 필요

# 변수 초기화
title = []
link = []
date = []
contents = []
comments = []

print('크롤링할 네이버 카페 주소를 입력해주세요.\n'
      '예시 : http://cafe.naver.com/joonggonara')
cafe_url = input(' > ').strip()
#cafe_url = 'http://cafe.naver.com/joonggonara'

print('Cookie 값을 입력 해주세요.\n'
      'Cookie 값은 Chrome 기준으로 Ctrl+Alt+i > Network 에서 확인 할 수 있습니다.')
cookie = input(' > ')

req = urllib.request.Request(
                cafe_url,
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )
req.add_header('Cookie', cookie)

gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
res = urllib.request.urlopen(req, context=gcontext)
doc = res.read().decode('MS949', 'ignore')

soup = BeautifulSoup(doc, 'html.parser')
# 게시판 검색
print('검색 할 대상 게시판을 입력해주세요.')
select_b = input(' > ').strip()
#select_b = '중나 평화연구소'

print('검색 결과의 페이지 수를 입력해주세요.\n'
      '(1페이지당 15개 출력)\n'
      '=> 2 입력 시 30개 출력')
chk = False
while chk == False:
    try:
        repeater = int(input(' > '))
        if 0 < repeater :
            chk = True
        else:
            print('\n올바른 값을 입력해주세요.')
            chk = False
    except ValueError:
        print('\n숫자만 입력해주세요.')
        chk = False
        pass

board_data = soup.find('div', attrs={'class': 'box-g-m'}).findAll('a', attrs={'class': 'gm-tcol-c'})

# 페이지 반복
for r in range (0, repeater):
    print ('현재, [', r+1 , '] 페이지를 작업중입니다.')
    if r != 0 :
        delay = random.random() * 10
        print ('안전한 크롤링을 위해 타이머를 작동합니다\n'
               '대기시간 : [', str(delay)[0:4], '] 초')
        time.sleep(delay)

    for i in range (1, len(board_data)):

        if str(board_data[i]).find(select_b) != -1 :
            tmp = str(board_data[i]).find('href=')
            tmp2 = str(board_data[i]).find('\"', tmp+6)
            target_url = str(board_data[i])[ tmp+6 : tmp2 ]
            tmp = target_url.find('clubid')
            tmp2 = target_url.find('&', tmp+1)
            clubid = target_url[ tmp + 7 :tmp2 ]
            tmp = target_url.find('menuid')
            tmp2 = target_url.find('&', tmp + 1)
            menuid = target_url[tmp + 7:tmp2]
            #http://cafe.naver.com/ArticleList.nhn?search.clubid=10050146&search.menuid=1256&search.page=2
            target_url = 'http://cafe.naver.com/ArticleList.nhn?search.clubid=' + clubid + '&search.menuid=' + menuid + '&search.page=' + str(r)
            #print("target url", target_url, "\nclubid:", clubid, "menuid", menuid)

    if (target_url == None):
        print('게시판을 찾을 수 없습니다.')

    # 타겟 게시판 open

    req = urllib.request.Request(
                    target_url,
                    data=None,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
                        'Cookie': cookie
                    }
                )


    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    res = urllib.request.urlopen(req, context=gcontext)
    doc = res.read().decode('MS949', 'ignore')

    soup = BeautifulSoup(doc, 'html.parser')

    #print(soup.prettify())

    # 게시판 공지부분을 뺀 데이터 파싱
    article_id = soup.find('form', attrs={'name':'ArticleList'}).findAll('span', attrs={'class': 'm-tcol-c'})
    article_link = []
    for i in range (0, len(article_id)):
        tmp = str(article_id[i]).find('>')
        tmp2 = str(article_id[i]).find('</')
        article_id[i] = str(article_id[i])[tmp+1:tmp2]
        #print("article_id",i," : ",article_id[i])
        article_link.append('http://cafe.naver.com/ArticleRead.nhn?clubid=' + clubid + '&menuid=' + menuid + '&articleid=' + article_id[i])

    # 게시글을 데이터로 내오는 부분
    for i in range(0, len(article_link)): #1을 len(article_link) 로 바꿀것
        req = urllib.request.Request(
                        article_link[i],
                        data=None,
                        headers={
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
                            'Cookie': cookie
                        }
                    )


        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        res = urllib.request.urlopen(req, context=gcontext)
        doc = res.read().decode('MS949', 'ignore')

        soup = BeautifulSoup(doc, 'html.parser')
        # 게시글의 제목을 파싱
        title_tmp = soup.find('div', attrs={'class' : 'tit-box'}).find('span', attrs={'class' : 'b m-tcol-c'}).text.strip()
        title.append(title_tmp)

        # 게시글의 주소 저장
        link.append(cafe_url + '/' + article_id[i])

        # 게시글의 작성일을 파싱
        date_tmp = soup.find('div', attrs={'class': 'tit-box'}).find('td', attrs={'class': 'm-tcol-c date'}).text.strip()
        date.append(date_tmp)

        # 게시글의 본문을 파싱
        contents_tmp = soup.find('div', attrs={'class': 'tbody m-tcol-c'}).text.strip()
        contents.append(contents_tmp)

        # 게시글의 댓글과 대댓글을 파싱 => AJAX로 인해 삭제
        #comments_tmp = soup.find('div', attrs={'class': 'box-reply2 bg-color u_cbox'})#.findAll('li')
        #.findAll('div', attrs={'class':'comm_cont'})

        #print(i, "번째 결과물\n", title[i], '\n', link[i], '\n', date[i], '\n', contents[i])


output = pd.DataFrame({'1. Title' : title,
                       '4. URL' : link,
                       '2. Date' : date,
                       '3. Contents' : contents })
print(output.head(10))
directory = os.path.dirname(os.path.abspath(__file__))
fileName = str(datetime.datetime.now().strftime('%Hh%Mm%Ss')) + '_' + cafe_url[22:len(cafe_url)] + '_NaverCafe_Result.csv'
finalPath = directory + '/output/' + str(datetime.datetime.today().strftime('%Y%m%d'))
if os.path.exists(finalPath) == False :
    os.makedirs(str(finalPath))
output.to_csv( finalPath + '/' + fileName + '.csv', sep= ',', encoding='utf-8')
print ("\n위와 같이 아래의 경로에 성공적으로 저장되었습니다.\n", directory + '/output/' + str(datetime.datetime.today().strftime('%Y%m%d')) + '/' + fileName)
