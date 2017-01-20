#-*- coding: utf-8 -*-
import urllib                       #URL을 열고 HTML을 읽는 모듈, urllib을 불러온다
from bs4 import BeautifulSoup       #bs4모듈에서 뷰티풀수프 함수를 불러옴

targetUrl = "http://naver.com"
soup = BeautifulSoup(urllib.urlopen(targetUrl).read()) #해당 웹주소 열고 뷰티풀수프로 긁어온 다음 soup라는 변수에 넣는다.
print soup #soup변수를 출력한다