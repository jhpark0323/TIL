import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import api_view


# A. CSV 데이터를 DataFrame으로 변환
df = pd.read_csv('static/data/test_data.csv', encoding='cp949')
dataframe = pd.DataFrame(df)

# B. 결측치 처리 후 데이터 변환
dataframe = dataframe.fillna('NULL')   # NaN -> NULL
# print(dataframe)

# C. 알고리즘 구현하기(평균 나이와 가장 비슷한 10명)

# '나이' 컬럼의 평균 계산
age_column = dataframe['나이']
dataframe['나이'] = pd.to_numeric(dataframe['나이'], errors='coerce')
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
# print(dataframe_top10_closest)
# print(dataframe)



# A. csv데이터 dataframe으로 변환
@api_view(['GET'])
def change_df(request):
    #CSV 파일의 상대 경로 생성
    data = dataframe.to_dict('records')

    context = {
        'data': data,
    }

    return JsonResponse(context)


# D. Loucst 를 활용한 알고리즘 성능 측정
@api_view(['GET'])
def loucst(request):
    #CSV 파일의 상대 경로 생성
    algorithm = new_dataframe.to_dict('records')

    context = {
        'algorithm': algorithm,
    }

    return JsonResponse(context)