from django.shortcuts import render,redirect
from .forms import KeywordForm
# Create your views here.

from .models import Keyword

import requests

from bs4 import BeautifulSoup

from selenium import webdriver

import re

from datetime import datetime
from .models import Trend, Keyword

import matplotlib.pyplot as plt

import base64
from io import BytesIO


def keyword(request):
    keyword = Keyword.objects.all()
    form = KeywordForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('trends:keyword')

    context = {
        'form':form,
        'keyword':keyword,
    }

    return render(request, 'trends/keyword.html', context)


def delete(request, pk):

    keyword = Keyword.objects.get(pk=pk)
    trends = Trend.objects.filter(name=keyword.name)


    keyword.delete()
    trends.delete()
    

    return redirect('trends:keyword')


def get_data(keyword, tool):
    if tool == 'all':
        url = f'http://www.google.com/search?q={keyword}'
    else:
        url = f'http://www.google.com/search?q={keyword}&tbs=qdr:y'
        
    # 동적인 페이지는 정상적으로 가져올 수 없다
    response = requests.get(url)

    # print(response.text)

    driver = webdriver.Chrome()
    driver.get(url)
    # 열린 페이지 소스들을 받아온다.
    html = driver.page_source
    # print(html)

    
    soup = BeautifulSoup(html, 'html.parser')
    # 눈으로 보기 좋게 출력
    # print(soup.prettify())

    # 각 게시물을 가져오자!
    # 공통적으로 div태그 + g클래스
    result_stats = soup.select_one("#result-stats").text
    print(result_stats)
    idx = result_stats.find('개')
    number = int(result_stats[7:idx].replace(',', ''))
    
    return number



def crawling(request):

    keyword_objects = Keyword.objects.all()
    
    for keyword in keyword_objects:
        num = get_data(keyword.name, 'all')
        Trend.objects.get_or_create(
            name=keyword.name,
            defaults={'result':num},
            search_period = 'all',
            )
    
        print(num)
    
    trends = Trend.objects.filter(search_period='all')

    context = {
        'trends':trends,
    }

    return render(request, 'trends/crawling.html', context)


def histogram(request):

    trends = Trend.objects.all()

    trends_dict = {}

    for trend in trends:
        trends_dict[trend.name] = trend.result


    plt.bar(trends_dict.keys(), trends_dict.values())
    # plt.show()

    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.grid(True)
    plt.legend()


    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    graph_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'graph_base64': f'data:image/png;base64, {graph_base64}'
    }


    return render(request, 'trends/crawling_histogram.html', context)

def advanced(request):
    keyword_objects = Keyword.objects.all()
    
    for keyword in keyword_objects:
        num = get_data(keyword.name, 'year')
        Trend.objects.get_or_create(
            name=keyword.name,
            defaults={'result':num},
            search_period = 'year',
            )
    
        print(num)
    
    trends = Trend.objects.filter(search_period = 'year')

    trends_dict = {}

    for trend in trends:
        trends_dict[trend.name] = trend.result


    plt.bar(trends_dict.keys(), trends_dict.values())
    # plt.show()

    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.grid(True)
    plt.legend()


    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    graph_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'graph_base64': f'data:image/png;base64, {graph_base64}'
    }
    return render(request, 'trends/crawling_advanced.html', context)