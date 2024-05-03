from django.http import JsonResponse
from rest_framework.decorators import api_view
import random

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

# -----------------------------------------------------------

import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import api_view



df = pd.read_csv('static/data/test_data.csv', encoding='cp949')
dataframe = pd.DataFrame(df)

# A. CSV 데이터를 DataFrame으로 변환
@api_view(['GET'])
def change_df(request):
    data = dataframe.to_dict('records')

    context = {
        'data': data,
    }

    return JsonResponse(context)


df_has_null = pd.read_csv('static/data/test_data_has_null.csv', encoding='cp949')
df_null = pd.DataFrame(df_has_null)

# B. 결측치 처리 후 데이터 변환
@api_view(['GET'])
def process_null(request):
    dataframe_null = df_null.fillna('NULL')   # NaN -> NULL
    data = dataframe_null.to_dict('records')

    context = {
        'data': data,
    }

    return JsonResponse(context)


# C. 알고리즘 구현하기(평균 나이와 가장 비슷한 10명)
@api_view(['GET'])
def locust(request):
    # '나이' 컬럼의 평균 계산
    age_average = dataframe['나이'].mean()

    # 평균과의 차이 계산 및 절대값 적용
    dataframe['평균과의 차이'] = (df['나이'] - age_average).abs()

    # 평균과의 차이에 따라 데이터프레임 정렬
    dataframe_sorted = dataframe.sort_values(by='평균과의 차이')

    # 상위 10개 데이터 추출
    dataframe_top10_closest = dataframe_sorted.head(10)

    # 결과 출력
    new_dataframe = dataframe_top10_closest.drop('평균과의 차이', axis=1)
    dataframe.drop('평균과의 차이', axis=1, inplace=True)
    print(new_dataframe)

    data = new_dataframe.to_dict('records')

    context = {
        'data': data,
    }

    return JsonResponse(context)


# D. Locust 를 활용한 알고리즘 성능 측정