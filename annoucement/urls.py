from django.urls import path
from . import views

app_name = 'annoucement'

urlpatterns = [
    path('list/', views.list, name='annoucement'),
]
