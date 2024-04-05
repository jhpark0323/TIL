from django.urls import path
from . import views

app_name = 'myapps'
urlpatterns = [
  path('', views.index, name='index'),
]
