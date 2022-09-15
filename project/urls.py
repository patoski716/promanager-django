from django.urls import path, include
from .views import *

urlpatterns = [
    path('clients/', ClientList.as_view(), name='listcreate'),
    path('clients/delete_client/<int:pk>/', delete_client.as_view()),
    path('projects/', ProjectList.as_view(), name='listcreate'),
    path('projects/delete_project/<int:pk>/', delete_project.as_view()),
]