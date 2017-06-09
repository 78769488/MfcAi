from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from byx.serializers import UserSerializers, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user的API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑group的API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

