from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response


from .models import Client,Project
from .serializers import ClientSerializer,ProjectSerializer

from rest_framework import generics

class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class delete_client(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class delete_project(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer