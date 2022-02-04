from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('notice_list/', views.list, name='notice_list'),
    # path('notice_newpost/', views.newpost, name='notice_newpost'),
    path('notice_newpost/', views.NoticeCreateView.as_view(), name='notice_newpost'),
]
