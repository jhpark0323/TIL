from django.urls import path
from . import views

urlpatterns = [
    path('', views.change_df),
    path('loucst/', views.loucst),
]

