from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from reminderapi.serializers import UserSerializer,TodoSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from reminder.models import Todos


from rest_framework import authentication
from rest_framework import permissions


# Create your views here.

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class TodosViewsetView(ViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Todos.objects.filter(user=request.user)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todos.objects.get(id=id)
        serializer=TodoSerializer(qs)
        return Response(data=serializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Todos.objects.get(id=id)
        serializer=TodoSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.filter().delete()
        return Response(data={"message":"todo deleted"})
    
    

        
        
    
