from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('notice_list/', views.list, name='notice_list'),
    path('notice_create/', views.create, name='notice_create'),
]
