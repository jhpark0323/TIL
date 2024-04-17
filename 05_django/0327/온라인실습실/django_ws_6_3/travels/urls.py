from django.urls import path
from . import views

app_name = 'travels'
urlpatterns = [
    path('create/',views.create,name="create"),
    path('<int:pk>/',views.detail,name="detail"),
    path('',views.index,name="index"),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>/update',views.update,name="update"),
]