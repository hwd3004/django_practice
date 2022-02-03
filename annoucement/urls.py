from django.urls import path
from . import views

app_name = 'annoucement'

urlpatterns = [
    path('list/', views.list, name='annoucement'),
    path('newpost/', views.newpost, name='newpost'),
    path('newpost2/', views.NewPost.as_view(), name='newpost2'),
]
