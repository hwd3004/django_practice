from django.urls import path
from .views import LabCreateView
from . import views

app_name = 'lab'

urlpatterns = [
    path('create/', LabCreateView.as_view(), name='create'),
    path('labcreate/', views.labcreate, name='labcreate'),
]
