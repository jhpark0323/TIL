from django.urls import path
from . import views


app_name = 'accounts'

'''
    주의 사항,
    문자열 variable routing 사용시,
    <username>/ 과 같이 작성했다면, 해당 경로는 urlpatterns 최하단에 작성
    왜냐..? urlpattenrs 리스트를 순회하면서, 순차적으로
    client가 입력한 문자열을 대조해볼려고 하는데... 
    <username>/ 해당 내용이 최상단 등에 있으면,,
    무슨 문자열을 집어넣든, 그 경로로 인식되어 버리기 때문이다.
'''
urlpatterns = [
    # path('url 경로/', 실행될 view함수, pattern 이름)
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # variable routing 사용 중...
    path('<str:username>/', views.profile, name='profile'),
    path('<int:profile_owner_pk>/follow/', views.follow, name='follow'),
]