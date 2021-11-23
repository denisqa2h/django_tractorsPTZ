from django.db.models import query
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView, UpdateAPIView)
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Accidents, UserProfile,AccidentsType, Buttons
from .permissions import IsAdmin, IsAdminAndOwner, IsMasterOrAdmin
from .serializers import AccidentsSerializer, ButtonsSerializer, ChangeTypeOfMeSerializer, ChangeTypeOfUsersSerializer, UserProfileSerializer, AccidentsTypeSerializer
from django.contrib.auth.models import Permission, User



class UserProfileListCreateView(ListCreateAPIView):
    """Просмотр и создание пользователя и сохранение в сериализацию, потом в базу (просмотр по всей коллекции)"""
    queryset=User.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes=[IsAdmin]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'user']
    ordering = ['id']

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение, удаление по одному экземпляру пользователей"""
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes=[IsAdmin]


class AccidentsTypeCreateView(ListCreateAPIView):
    """Создание происшествия и просмотр всей коллекции"""
    queryset=AccidentsType.objects.all()
    serializer_class=AccidentsTypeSerializer
    permission_classes=[IsMasterOrAdmin]
    filter_backends = [OrderingFilter]
    ordering = ['id']


class AccidentsTypeDetailView(RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение, удаление по одному экземпляру происшествий"""
    queryset=AccidentsType.objects.all()
    serializer_class=AccidentsTypeSerializer
    permission_classes=[IsMasterOrAdmin]


class ChangeTypeOfUsersView(UpdateAPIView, ListAPIView, ListCreateAPIView):
    """Просмотр всех экземпляров пользователей. Изменение и удаление по одному экземпляру"""
    queryset=User.objects.all()
    serializer_class=ChangeTypeOfUsersSerializer
    permission_classes=[IsAdmin]
    filter_backends = [OrderingFilter] 
    ordering_fields = ['id', 'username'] 
    ordering = ['-id']

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class DeletingUsersView(DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=ChangeTypeOfUsersSerializer
    permission_classes=[IsAdminAndOwner]


class ButtonsView(ListAPIView):
    queryset=Buttons.objects.all()
    serializer_class=ButtonsSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering = ['id']


class AccidentsCheckView(ListCreateAPIView):
    queryset=Accidents.objects.all()
    serializer_class=AccidentsSerializer
    permission_classes=[IsMasterOrAdmin]
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering_fields=['id', 'FixTime', 'EndTime', 'Post', 'Description']
    search_fields=['id', 'FixTime', 'EndTime', 'Post', 'Description']
    filter_fields=['id', 'FixTime', 'EndTime', 'Post', 'Description']
    ordering = ['-id']


class AccidentsChangeView(RetrieveUpdateAPIView):
    queryset=Accidents.objects.all()
    serializer_class=AccidentsSerializer
    permission_classes=[IsMasterOrAdmin]
    
    

    
    """
    def get(self, request):
        queryset = self.get_queryset()
        serializer_for_queryset = ChangeTypeOfUsersSerializer(queryset, many=True)
        if self.permission_classes == [IsAdmin]:
            return Response({"UserRoles":serializer_for_queryset.data})
    """


