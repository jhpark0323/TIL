import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"

    # 동적인 페이지는 정상적으로 가져올 수 없다!
    # response = requests.get(url)
    # print(response.text)

    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)
    # 열린 페이지 소스들을 받아온다.
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 검색 결과 개수
    # result-stats id 를 사용
    result_stats = soup.select_one("#result-stats")
    print(result_stats.text)
    

keyword = "탕수육"
get_data(keyword)
