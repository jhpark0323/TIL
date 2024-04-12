# 4/12 PJT 5 - 금융
## 키워드 검색량 분석을 위한 데이터 수집

### 준비사항

- VSCode
- 강한 정신력
- ChatGPT
- requirements.txt

```md
asgiref==3.8.1
attrs==23.2.0
beautifulsoup4==4.12.3
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
contourpy==1.2.1
cycler==0.12.1
Django==4.2.11
exceptiongroup==1.2.0
fonttools==4.51.0
h11==0.14.0
idna==3.7
importlib_resources==6.4.0
kiwisolver==1.4.5
matplotlib==3.8.4
numpy==1.26.4
outcome==1.3.0.post0
packaging==24.0
pillow==10.3.0
pycparser==2.22
pyparsing==3.1.2
PySocks==1.7.1
python-dateutil==2.9.0.post0
requests==2.31.0
selenium==4.19.0
six==1.16.0
sniffio==1.3.1
sortedcontainers==2.4.0
soupsieve==2.5
sqlparse==0.4.4
trio==0.25.0
trio-websocket==0.11.1
typing_extensions==4.11.0
tzdata==2024.1
urllib3==2.2.1
wsproto==1.2.0
zipp==3.18.1
```
---

### 프로젝트 과정
---

#### 기본 설정

- 가상환경 설정

- Django 프로젝트 명 : mypjt

- Django 앱 명 : trends

- gitignore 필수

- 구글 크롤링

- 구글 크롤링(1년간의 데이터)

---
#### urls, views, templates 생성

- base.html: 
  - 다른 파일 템플릿 경로로 이동할 수 있는 링크들을 출력

- keyword.html: 
  - 검색하고자 하는 키워드를 추가 및 삭제할 수 있도록 구성
  - 생성하기 및 삭제하기 버튼을 통해, Keyword 테이블에 데이터를 저장 및 삭제하도록 구성

- crawling.html: 
  - Keyword 테이블에 저장된 키워드들을 활용하여 크롬 검색 결과 페이지 크롤링을 수행
  - 페이지의 정보 중 “검색 결과 개수” 를 추출하여 Trend 테이블에 저장
  - 저장 시 검색 기간(search_period)을 “all” 로 저장
  - 저장 시 이미 저장되어 있는 키워드라면, 새로 생성하지 않고 검색 결과 개수를 변경

- crawling_histogram.html: 
  - 전체 기간 검색 결과를 이용하여 막대 그래프를 출력
  -  크롤링을 다시 진행하지 않고, Trend 테이블에 저장된 데이터를 활용

- crawling_advaned.html
  - 검색 결과 페이지 중 “지난 1년” 을 기준으로 필터링하여 크롤링을 수행

---

### 프로젝트 도중 어려웠던 점, 아쉬웠던 점

- 크롤링이라는 것을 이해하는 데에 어려움을 겪음

- 여러 라이브러리들을 import 했는데 그 라이브러리들을 활용하는 데에 어려움을 겪음

- ChatGPT도 말을 안들음

- 코드를 정확하게 작성해도 서버를 돌렸을 때 에러가 나는 경우가 있다.
  - 다시 새로고침을 하면 되는 경우가 많았다. 왜 인지는 모른다. 
---
### 소감

- 크롤링을 하는 데에서 많은 어려움을 겪었다.
- 다시 matplotlib을 사용했는데 이전 프로젝트에서 했던 경험이 도움이 되었다.


