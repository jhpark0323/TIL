# 08_pjt

### Test 1.
#### 총 접속자 : 100 | 동시 접속자 : 10


**[ver1. 함수]**  
  평균 RPS : 48.8  
  응답 시간 : Median 24ms, Average 75ms

**[ver2. 전역변수]**  
  평균 RPS :  50.5  
  응답 시간 : Median 3ms, Average 3ms


### Test 2.
#### 총 접속자 : 100 | 동시 접속자 : 10


**[ver1. 함수]**  
  평균 RPS : 40.8  
  응답 시간 : Median 6400ms, Average 6883ms

**[ver2. 전역변수]**  
  평균 RPS :  200.2  
  응답 시간 : Median 5ms, Average 6ms


### Test 3.
#### 총 접속자 : 100 | 동시 접속자 : 10


**[ver1. 함수]**  
  평균 RPS : 42.7  
  응답 시간 : Median 3300ms, Average 2707ms

**[ver2. 전역변수]**  
  평균 RPS :  100.1  
  응답 시간 : Median 5ms, Average 14ms

--------------------------

#### [알고리즘 별 성능 차이가 나는 이유]

ver1. 함수 : 함수안에 모든 계산을 다 넣어 실행할 때 마다 다시 dataframe을 만들어서 성능이 좋지 않음

ver2. 전역변수설정 : 전역변수로 dataframe을 만들어 놓아서 함수 실행시 response만 하면 되어 성능이 좋음

