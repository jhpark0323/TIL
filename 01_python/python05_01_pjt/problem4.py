import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


import pprint
import requests

# 전체 정기예금의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
  api_key = "API-KEY받기"

  url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
     'auth' : api_key,
     # 금융회사 코드 0200000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
     'topFinGrpNo' : '020000',
     'pageNo' : 1
  }
  # 요구사항에 맞도록 이곳의 코드를 수정합니다.

  response = requests.get(url, params=params).json()
  base = response['result']['baseList']

  # baseList의 금융상품코드, 금융상품명, 금융회사명을 담을 dict들을 모을 빈 list생성
  base_list = []

  for i in range(len(base)):
    # baseList의 금융상품코드, 금융상품명, 금융회사명을 담을 dict
    base_dict = {}
    base_dict['금융상품코드'] = base[i]['fin_prdt_cd']
    base_dict['금융상품명'] = base[i]['fin_prdt_nm']
    base_dict['금융회사명'] = base[i]['kor_co_nm']
    base_list.append(base_dict)

  # 여기까지 base_list에 다 담음 (성공)


  # option 관련 코드
  option = response['result']['optionList']

  option_list = []

  for options in range(len(option)):
    option_dict = {}
    option_dict['금융상품코드'] = option[options]['fin_prdt_cd']
    option_dict['저축 금리'] = option[options]['intr_rate']
    option_dict['저축 기간'] = option[options]['save_trm']
    option_dict['저축금리유형'] = option[options]['intr_rate_type']
    option_dict['저축금리유형명'] = option[options]['intr_rate_type_nm']
    option_dict['최고 우대금리'] = option[options]['intr_rate2']
    
    option_list.append(option_dict)

  # 금융상품코드가 같은 것들끼리 묶기
  # if 전에 있던 항목과 코드가 같으면 list로 추가
  # elif 다르면 새로운 list 생성 

  # 금융상품코드를 기준으로 정렬 
  option_list = sorted(option_list, key=lambda x: x['금융상품코드'])

  rate_info = {}
  rate_info_each = []
  for i in range(len(option_list)):
    
    rate_info_each_dict = {}
    if len(rate_info_each) == 0:
      rate_info_each_dict['저축 금리'] = option_list[i]['저축 금리']
      rate_info_each_dict['저축 기간'] = option_list[i]['저축 기간']
      rate_info_each_dict['저축금리유형'] = option_list[i]['저축금리유형']
      rate_info_each_dict['저축금리유형명'] = option_list[i]['저축금리유형명']
      rate_info_each_dict['최고 우대금리'] = option_list[i]['최고 우대금리']
      rate_info_each.append(rate_info_each_dict)
    
# 상품코드가 하나짜리인게 있는데 그것도 append시켜야함

    elif option_list[i]['금융상품코드'] == option_list[i-1]['금융상품코드']:
      rate_info_each_dict['저축 금리'] = option_list[i]['저축 금리']
      rate_info_each_dict['저축 기간'] = option_list[i]['저축 기간']
      rate_info_each_dict['저축금리유형'] = option_list[i]['저축금리유형']
      rate_info_each_dict['저축금리유형명'] = option_list[i]['저축금리유형명']
      rate_info_each_dict['최고 우대금리'] = option_list[i]['최고 우대금리']
      rate_info_each.append(rate_info_each_dict)

    elif option_list[i]['금융상품코드'] != option_list[i-1]['금융상품코드']:
      rate_info[option_list[i-1]['금융상품코드']] = rate_info_each
      rate_info_each = []
      rate_info_each_dict['저축 금리'] = option_list[i]['저축 금리']
      rate_info_each_dict['저축 기간'] = option_list[i]['저축 기간']
      rate_info_each_dict['저축금리유형'] = option_list[i]['저축금리유형']
      rate_info_each_dict['저축금리유형명'] = option_list[i]['저축금리유형명']
      rate_info_each_dict['최고 우대금리'] = option_list[i]['최고 우대금리']
      rate_info_each.append(rate_info_each_dict)

    if i == len(option_list)-1:
      rate_info[option_list[i-1]['금융상품코드']] = rate_info_each
  
  result = []

  for i in range(len(rate_info)):
    each_dict = {}
    each_dict['금리정보'] = rate_info[base_list[i]['금융상품코드']]
    each_dict['금융상품명'] = base_list[i]['금융상품명']
    each_dict['금융회사명'] = base_list[i]['금융회사명']
    result.append(each_dict)

  return result
  

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)