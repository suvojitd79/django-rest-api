from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User
from .serializers import user_serializers
import json
from rest_framework import viewsets
from rest_framework.views import APIView

class getAll(APIView):
    queryset = User.objects.all()
    def get(self,request):
        return HttpResponse('454')



