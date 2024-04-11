from django.urls import path
from . import views

urlpatterns = [
  path('libraries/', views.library_list),
  path('libraries/<int:pk>/', views.detail),
]
