'''
[ version 0.1 ]
created: 2017.01.23.
release: 2017.01.xx.
- 네이버 검색 : 블로그 기준으로 데이터 크롤링
- 크롤링 한 도큐먼트를 파싱하여 데이터 정제

+ 앞으로 추가/수정 할 것들
- 사용자에게 입력 받아서 검색 방법 및 검색 결과를 조정 할 것
- 검색 결과 정할 수 있도록 할 것
- csv , txt 파일 등으로 저장 할 수 있도록 할 것
- 상세검색 기능
- 블로그 외 네이버 검색의 뉴스, 카페 검색 기능
- 쿠키를 이용 or Selenium을 이용하여 사용자의 아이디로 가입한 네이버 카페 내 게시물 크롤링 할 수 있도록 하는 기능
- 모바일 버전에서 검색 할 경우의 검색 결과(노출 순서가 다르기 때문)
- 클래스를 사용하도록 수정 할 것(recommended)
'''

#-*- coding: utf-8 -*-
import urllib.request
import ssl
import datetime

from bs4 import BeautifulSoup       # Beautiful Soup 설치 필요

def main():
    query = urllib.request.quote('아이폰')
    blog = 'http://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query='
    doc = getHTML(blog + query)
    title, link, date, contents, blogName = parseNS_blog(doc)
    # 이후 도큐먼트로 output 할 것.
    for i in range(0, len(title)):
        print(i+1,'번쨰 결과물')
        print(title[i], '\n' ,link[i], '\n' , date[i], '\n' , contents[i], '\n' , blogName[i])

def getHTML(targetURL):
    try:
        req = urllib.request.Request(
            targetURL,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        res = urllib.request.urlopen(req, context=gcontext)
        doc = res.read().decode('utf-8')

        soup = BeautifulSoup(doc, 'html.parser', from_encoding='utf-8')
        return soup

    except urllib.request.HTTPError as e:
        print ("HTTP error: %d" % e.code)
        return None

    except urllib.request.URLError as e:
        print ("URL error: %d" % e.code)
        return None

def parseNS_blog(soup):  #parse Naver Search -> title, link, date, contents, blogName

    title = soup.findAll('li', attrs={'class':'sh_blog_top'})    # 글 제목과 링크를 포함한 부분
    date = soup.findAll('dd', attrs={'class': 'txt_inline'})
    contents = soup.findAll('dd', attrs={'class': 'sh_blog_passage'})
    blogName = soup.findAll('a', attrs={'class': 'txt84'})
    link = [0,1,2,3,4,5,6,7,8,9]
    #print(title[0])

    for i in range (0, len(title)): # title 과 link 데이터 파싱
        #print(title[i])
        tmp = str(title[i]).find('href=')
        tmp2 = str(title[i]).find('\"', tmp)
        tmp3 = str(title[i]).find('\"', tmp2 + 1)
        link[i] = str(title[i])[tmp2 + 1:tmp3]
        tmp = str(title[i]).find('title=')
        tmp2 = str(title[i]).find('\"', tmp)
        tmp3 = str(title[i]).find('\"', tmp2+1)
        title[i] = str(title[i])[tmp2 + 1:tmp3]

    for i in range (0, len(date)):  # date 데이터 파싱
        tmp = str(date[i]).find('>')
        tmp2 = str(date[i]).find('<div')
        date[i] = str(date[i])[tmp + 1 : tmp2]
        # 추가한 부분 : 'n일 전 ' 으로 나오는 부분을 날짜로 변경
        if (str(date[i]).find('일') != -1):
            date[i] = (datetime.date.today() - datetime.timedelta( days=+ int(str(date[i])[0]) )).strftime('%Y.%m.%d')

    for i in range (0, len(contents)):
        tmp = str(contents[i]).find('>')
        tmp2 = str(contents[i]).find('</dd')
        contents[i] = str(contents[i])[tmp + 1 : tmp2]
        for j in range (0, str(contents[i]).count('<strong class=\"hl\">')):
            contents[i] = str(contents[i]).replace('<strong class=\"hl\">','')
            contents[i] = str(contents[i]).replace('</strong>', '')

    for i in range (0, len(blogName)):
        tmp = str(blogName[i]).find('>')
        tmp2 = str(blogName[i]).find('</a')
        blogName[i] = str(blogName[i])[tmp + 1 : tmp2]

    for i in range (0, blogName.count('블로그 내 검색')):
        blogName.remove('블로그 내 검색')

    return title, link, date, contents, blogName

main()