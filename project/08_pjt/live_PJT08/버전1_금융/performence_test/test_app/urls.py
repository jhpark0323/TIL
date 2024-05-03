from django.urls import path
from . import views

urlpatterns = [
    # 내장 메서드 sort()
    path('normal_sort/', views.normal_sort),
    # 우선순위큐
    path('priority_queue/', views.priority_queue),
    # 버블정렬
    path('bubble_sort/', views.bubble_sort),
]

