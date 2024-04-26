import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import WeatherSerializer
from .models import Weather

api_key = settings.WEATHER_API_KEY

# A. 서울의 5일 치 예보 데이터 확인
def index(request):
    city_name = 'Seoul,KR'

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    return JsonResponse(response)


# B. 원하는 데이터만 DB에 저장
def save_data(request):
    city_name = 'Seoul,KR'

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()

    for li in response.get('list'):
        # 원하는 데이터 추출하기
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')

        # 항상 확인부터!
        # print('dt_txt = ', dt_txt)
        # print('temp = ', temp)
        # print('feels_like = ', feels_like)

        save_data = {
            'dt_txt': dt_txt,
            'temp': temp,
            'feels_like': feels_like,
        }

        serializer = WeatherSerializer(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면, 저장
            serializer.save()

    return JsonResponse({ "message": "save okay!" })


@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()
    serializers = WeatherSerializer(weathers, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def hot_weathers(request):
    # 단순한 방법
    # 1. 전체를 가져온다
    # weathers = Weather.objects.all()
    # # 2. 새로운 리스트에다가 조건에 맞는 데이터만 추가한다
    # hot_weathers = []
    # for weather in weathers:
    #     # 섭씨온도가 20도가 넘으면 hot_weathers 에 추가
    #     celsius = round(weather.temp - 273.15, 2)
    #     if celsius > 20:
    #         hot_weathers.append(weather)

    # # 3. 포장해서 반환다.
    # serializers = WeatherSerializer(hot_weathers, many=True)
    # return Response(serializers.data)

    # 권장 방식
    weathers = Weather.objects.filter(temp__gt=(20 + 273.15))
    serializers = WeatherSerializer(weathers, many=True)
    return Response(serializers.data)
