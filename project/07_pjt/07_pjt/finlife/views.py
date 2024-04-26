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