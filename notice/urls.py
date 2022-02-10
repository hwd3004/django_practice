from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('notice_list/', views.list, name='notice_list'),
    path('notice_create/', views.create, name='notice_create'),
    path('notice/<int:pk>/', views.detail, name='notice_detail'),
    path('notice_update/<int:pk>/', views.update, name='notice_update'),
    path('notice_delete/<int:pk>/', views.delete, name='notice_delete'),
    path('notice_removeHasAttach/', views.removeHasAttach, name='notice_removeHasAttach')
]
