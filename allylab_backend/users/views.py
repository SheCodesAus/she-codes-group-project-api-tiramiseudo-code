from re import X
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, Skill
from .serializers import CustomUserSerializer, SkillSerializer,CustomUserDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly
import json

class CustomUserList(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
    
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response("Oops! You've missed some fields when you tried to create your account.", status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):

    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserDetailSerializer (user)
        return Response(serializer.data)

class SkillList(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserSerializer(instance=user,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()

class SkillDetail(APIView):

    def get(self, request, pk):
        skill = Skill.objects.get(pk=pk)
        serializer = SkillSerializer (skill)
        return Response(serializer.data)

class Hello(APIView):
    def get(self, request):
        data = '{"String":"Hello Allylab!" }'
        y = json.loads(data)
        return Response(y)