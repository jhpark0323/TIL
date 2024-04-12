from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
from .models import Article, Query


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

    # 각 게시물을 가져오자!
    # 공통적으로 div태그 + g클래스
    g_list = soup.select('div.g')

    results = []
    for g in g_list:
        # 요소 안에서 LC20lb MBeuO DKV0Md 클래스를 가진 특정 요소 선택
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")
        # 요소가 존재 한다면
        if title is not None:
            # print('제목 = ', title.text)
            results.append(title.text)

    return results



# Create your views here.
def crawling(request):
    keyword = "탕수육"
    titles = get_data(keyword)
    results = []
    for title in titles:
        # get_or_create : 있다면 조회, 없다면 생성
        # 1. article 저장
        #   - 기존에 이미 저장된 article 이면 pass
        article, created_article = Article.objects.get_or_create(title=title)
        # 2. keyword 저장        
        #   - 기존에 이미 저장된 keyword 면 pass
        query_obj, created_query = Query.objects.get_or_create(article=article, keyword=keyword)
        results.append(title)
    
    
    context = {
        'results': results,
    }

    return render(request, 'apps/index.html', context)
