
from django.shortcuts import render, redirect
import pandas as pd
# Create your views here.
import matplotlib.pyplot as plt

import base64
from io import BytesIO

plt.switch_backend('Agg')


def problem1(request):
    csv_path = 'weathers/austin_weather.csv'
    data = pd.read_csv(csv_path)

    df = pd.DataFrame(data)
    data['Date'] = pd.to_datetime(data['Date'])

    context = {
        'df':df,
    }

    return render(request, 'weathers/problem1.html', context)


def problem2(request):
    # CSV 파일 경로 설정
    csv_path = 'weathers/austin_weather.csv'
    
    # CSV 파일을 Pandas 데이터프레임으로 읽기
    data = pd.read_csv(csv_path)
    
    # 'Date' 열을 datetime 형식으로 변환
    data['Date'] = pd.to_datetime(data['Date'])
    
    dc = data.loc[:, ['Date', 'TempHighF', 'TempAvgF', 'TempLowF']]
    print(dc)
    dc['TempHighF'] = dc['TempHighF'].astype(int)
    dc['TempAvgF'] = dc['TempAvgF'].astype(int)
    dc['TempLowF'] = dc['TempLowF'].astype(int)
    
    plt.clf()
    plt.plot(dc['Date'], dc['TempHighF'], label='High Temperature')
    plt.plot(dc['Date'], dc['TempAvgF'], label='Average Temperature')
    plt.plot(dc['Date'], dc['TempLowF'], label='Low Temperature')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.grid(True)
    
    # legend 추가
    plt.legend()
    
    # 그래프를 이미지로 저장하여 Base64로 인코딩
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    graph_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    # 생성한 그래프 이미지 Base64 데이터를 컨텍스트에 추가
    context = {
        'graph_base64': f'data:image/png;base64, {graph_base64}'
    }
    
    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    csv_path = 'weathers/austin_weather.csv'
    
    # CSV 파일을 Pandas 데이터프레임으로 읽기
    data = pd.read_csv(csv_path)
    
    # 'Date' 열을 datetime 형식으로 변환
    data['Date'] = pd.to_datetime(data['Date'])

    
    dc = data.loc[:, ['Date', 'TempHighF', 'TempAvgF', 'TempLowF']]
    print(dc)
    dc['TempHighF'] = dc['TempHighF'].astype(int)
    dc['TempAvgF'] = dc['TempAvgF'].astype(int)
    dc['TempLowF'] = dc['TempLowF'].astype(int)
    
    monthly_avg_temp = dc.resample('M', on='Date').mean()
    plt.clf()
    plt.plot(monthly_avg_temp.index, monthly_avg_temp['TempHighF'], label='High Temperature')
    plt.plot(monthly_avg_temp.index, monthly_avg_temp['TempAvgF'], label='Temperature')
    plt.plot(monthly_avg_temp.index, monthly_avg_temp['TempLowF'], label='Low Temperature')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.grid(True)
    
    # legend 추가
    plt.legend()
    
    # 그래프를 이미지로 저장하여 Base64로 인코딩
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    graph_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    # 생성한 그래프 이미지 Base64 데이터를 컨텍스트에 추가
    context = {
        'graph_base64': f'data:image/png;base64, {graph_base64}'
    }
    
    return render(request, 'weathers/problem3.html', context)

def problem4(request):

    csv_path = 'weathers/austin_weather.csv'
    
    # CSV 파일을 Pandas 데이터프레임으로 읽기
    data = pd.read_csv(csv_path)

    data['Events'] = data['Events'].replace(' ', 'No Events')
    print(data)

    # "Events" 열에서 각 이벤트를 분리하여 새로운 행으로 만듦
    events = data['Events'].str.split(' , ')
    data_expanded = data.loc[events.index.repeat(events.apply(len))]
    data_expanded['Event'] = [event for sublist in events.tolist() for event in sublist]

    # 각 이벤트의 개수 세기
    grouped = data_expanded.groupby('Event').size().reset_index(name='Count')

    grouped = grouped.sort_values(by='Count', ascending=False)
    # 그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(grouped['Event'], grouped['Count'])
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    # plt.xticks(rotation=45)
    plt.grid(True)
    
    # 그래프를 이미지로 저장하여 Base64로 인코딩
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    graph_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    # 생성한 그래프 이미지 Base64 데이터를 컨텍스트에 추가
    context = {
        'graph_base64': f'data:image/png;base64, {graph_base64}'
    }
    
    return render(request, 'weathers/problem4.html', context)


