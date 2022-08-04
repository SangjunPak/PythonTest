from urllib.request import urlopen
from bs4 import BeautifulSoup

#뉴스기사 검색 URL -> 아래의 경우에는 naver에 파이썬 검색 -> 뉴스 탭으로 이동한 뒤 복사한 URL 
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&oquery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&tqi=hBfMbsp0JywssgLt3sNssssstPC-098999"

# urlopen 함수를 통해 url주소를 open 하여 읽고, 그 값을 html 이라는 변수에 저장 합니다.
html = urlopen(url).read()

# html 정보가 담겨있는 변수를 bs4 라이브러리에 있는 BeautifulSoup을 이용해
# html 정보를 parsing 하여 soup 에 저장합니다.
soup = BeautifulSoup(html, 'html.parser')

# parsing된 결과인 soup 에서 news_tit class ( 뉴스 제목 클래스를 의미 함) 를 검색하고, 가장 첫번째 값을 반환 합니다.
first_found = soup.find(class_='news_tit') # html에서 news_area 이라는 클래스로 되어있는 정보 중 첫 번째 값을 반환
print(first_found.text)
#print(html_class)

