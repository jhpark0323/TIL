# 1. 기본세팅
- project : mypjt
- app : finlife
- .gitignore 세팅

## A. Model
- DepositProducts
- DepositOptions
  
```py
from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField() 

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField(default=-1)
    save_trm = models.IntegerField()
```

## B. Serializer
- DepositProductsSerializer
- DepositOptionsSerializer
```py
from rest_framework import serializers
from .models import DepositOptions, DepositProducts

class DepositProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)
```

# 2. API 불러오기
- 환경변수 관리!!! -> 몰랐던 부분
- pip install django-environ
- .env 파일작성

.env
```
API_KEY='...'
```
- settings.py에 추가

settings.py
```py
import os
import environ

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
API_KEY = env('API_KEY')
```

- 변수 사용 방법
```py
from django.conf import settings
api_key = settings.API_KEY
```

- views.py

views.py
```py
import requests
from django.db.models import Max
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer

api_key = settings.API_KEY

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = int(li.get('join_deny'))
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'etc_note' : etc_note,
            'join_deny' : join_deny,
            'join_member' : join_member,
            'join_way' : join_way,
            'spcl_cnd' : spcl_cnd,
        }

        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = float(li.get('intr_rate'))
        intr_rate2 = float(li.get('intr_rate2'))
        save_trm = int(li.get('save_trm'))

        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm' : intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'save_trm' : save_trm,
        }

        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=DepositProducts.objects.get(fin_prdt_cd=li.get('fin_prdt_cd')))

    return JsonResponse({ "message": "save okay!" })

@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    deposit_product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(deposit_product, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
    max_value = DepositOptions.objects.aggregate(max_value=Max('intr_rate2'))['max_value']
    print(max_value)
    products = DepositOptions.objects.filter(intr_rate2__gte=(max_value))
    serializer = DepositOptionsSerializer(products, many=True)

    return Response(serializer.data)
```
- save_deposit_products의 url과 response 잘 보기
- 직접 들어가서 자료 확인 후 원하는 부분 찾기

