from django.urls import path
from . import views

app_name = 'notice2'

urlpatterns = [
    path('notice2_list/', views.list, name='notice2_list'),
    path('notice2_create/', views.create, name='notice2_create'),
]
