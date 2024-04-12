import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/tag/love/'

# 1. 다운로드 - url 을 이용해서, HTML 이 담긴 자료를 받아와야 함
response = requests.get(url)

# html 문서를 text 형태로 확인
html_text = response.text

# str 이 출력된다.
print(type(html_text))

# 문자열 파싱은 코드로 짜기 매우 복잡하다.
# 라이브러리를 쓰자!
soup = BeautifulSoup(html_text, 'html.parser')

# bs4.BeautifulSoup class 가 출력됨
print(type(soup))

# 1. find
# - 첫 번째 태그를 가진 요소를 검색
main = soup.find('title')
print(main)

# 2. find_all
# - 해당 태그를 가진 모든 요소를 검색
# - 리스트로 반환된다.
a_tags = soup.find_all('a')
print(a_tags)

# 3. CSS 선택자로 하나를 선택
# 선택자가 일치하는 첫 번 째 글
# span 태그로도 검색이 가능하지만
# 인용구 라는 내용은 text class 로 지정
# 따라서, class 를 통한 검색이 더 옳다!
word = soup.select_one('.text')
print(f'첫 번째 글 = {word.text}')

# 4. CSS 선택자로 여러개를 선택
# 모든 인용구를 검색
words = soup.select('.text')
for w in words:
    print(f'글 : {w.text}')
