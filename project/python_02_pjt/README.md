# 02_pjt

### 넷플릭스 주가 데이터 분석

1. 데이터 전처리 - 데이터 읽어오기
```python
df = pd.read_csv('NFLX.csv')
df
# ()안에는 경로 넣기
```

2. 데이터 전처리 - 2021년 이후의 종가 데이터 출력하기

  - 2021년 이후 데이터 출력하기
```python
date2 = '2021-01-01'
# to_datetime으로 데이터 타입을 변경
date2_datetime = pd.to_datetime(date2)

df_b = df_a[df_a['Date'] >= date2_datetime]

```

- 그래프 그리기 
```python
# 그래프 그리기(가로축 : 날짜, 세로축 : 종가)
plt.plot(df_b['Date'], df_b['Close'])

# 그래프 제목
plt.title('NFIX Close Price')

# x축 레이블
plt.xlabel('Date')

# x 축 설정(회전시키기)
plt.xticks(rotation=45)

# y축 레이블
plt.ylabel('Close Price')

# 그래프 표시
plt.show()
```

3. 데이터 분석 - 2021년 이후 최고, 최저 종가 출력하기
```python
# max, min 함수를 이용해 최고 최저가 출력
max_price = df_b['Close'].max()
print(max_price)
min_price = df_b['Close'].min()
print(min_price)
```

4. 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기

- 월별로 그룹화
```python
# 기간을 'M'(month)로 변경 후 groupby를 이용해 그룹화 
df_mean = df_b.groupby(df_b['Date'].dt.to_period("M")).mean()
```

- index 타입 변경
```python
# 월별로 그룹화 할 때 index를 period로 바꿨는데 그러면 plt의 축으로 못씀 -> timestamp로 변경
df_mean.index = df_mean.index.to_timestamp()
df_mean
```

- 그래프 그리기
```python
# 그래프 그리기(가로축 : 날짜, 세로축 : 종가)
plt.plot(df_mean.index, df_mean['Close'])

# 그래프 제목
plt.title('Monthly Average Close Price')

# x축 레이블
plt.xlabel('Date')

# x 축 설정(회전시키기)
plt.xticks(rotation=45)

# y축 레이블
plt.ylabel('Average Close Price')

# x 축을 날짜 형식으로 인식하도록 설정
plt.gca().xaxis_date()

# 그래프 표시
plt.show()
```

5. 데이터 시각화 2022년 1월 이후 최고, 최저, 종가 시각화

- 2022년 이후 데이터 출력하기
```python
date22 = '2022-01-01'
date22_datetime = pd.to_datetime(date22)

df_e = df_a[df_a['Date'] >= date22_datetime]
```

- 그래프 그리기
```python
# 그래프 그리기
plt.plot(df_e['Date'], df_e['Close'], label='High')
plt.plot(df_e['Date'], df_e['Low'], label='Low')
plt.plot(df_e['Date'], df_e['High'], label='Close')

# 그래프 제목 설정
plt.title('High, Low and Close Prices since January 2022')

# x축 레이블 설정
plt.xlabel('Date')

# x 축 설정(회전시키기)
plt.xticks(rotation=45)

# y축 레이블 설정
plt.ylabel('Price')

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()
```

### TIL

1. 전체 dataframe을 읽고 원하는 열들만 읽어오기
2. to_datetime()으로 데이터 타입을 변경해보기
3. dataframe에서 조건을 주어 원하는 행들만 읽어오기
4. matplotlib을 사용해 시각화 하기
5. groupby를 이용해 월 별 그룹화 하기
6. 여러개의 그래프를 한번에 그려보기

### 느낀점

chat gpt, 구글링 등을 활용해 기억이 안나는 함수들 찾아 사용하기 -> 억지로 기억해낼 필요 없음

