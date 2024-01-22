import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    # 각각의 변수들을 parsed_data에서 가져옴
    name = parsed_data['name']
    lat = parsed_data['address']['geo']['lat']
    lng = parsed_data['address']['geo']['lng']
    company = parsed_data['company']['name']

    # 빈 dict에 각각을 넣어서 dict 형태로 만들어 dummy_data에 넣기
    dummy_dict = {}
    if ((float(lat) < 80) & (float(lat) > -80)) & (float(lng) < 80) & (float(lng) > -80):
        dummy_dict = {'company' : company, 'lat' : lat, 'lng' : lng, 'name' : name}
        dummy_data.append(dummy_dict)
    # print(parsed_data)

print(dummy_data)