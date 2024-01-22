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

# print(dummy_data)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def censorship(company_name, user_name):
    if company_name in black_list:
        print(f"{company_name} 소속의 {user_name} 은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상 없습니다.')
        return True

# censored_user_list 생성
censored_user_list = {}

def create_user(ls):
    for i in ls:
        if censorship(i['company'], i['name']):
            censored_user_list[i['company']] = [i['name']]

create_user(dummy_data)
print(censored_user_list)


