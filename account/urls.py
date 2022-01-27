from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='account'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('checkid/', views.checkid, name='checkid'),
    path('findid/', views.findid, name='findid'),
]
