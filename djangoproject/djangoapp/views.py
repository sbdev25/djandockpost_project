from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from serializers import UserSerializer
# Create your views here.
#get
@api_view(['GET'])
def getUsers(request) : 
    users = User.objects.all()
    serializer = UserSerializer(users , many=True)
    return Response(serializer.data)
#getPK
@api_view(['GET'])
def getUser_pk(request , pk):
    user = User.objects.get(pk = pk )
    serializer  = UserSerializer(user , many=False)
    return Response(serializer.data)
#post

@api_view(['POST'])
def addUser(request): 
    serializer  = UserSerializer(data=request.data)

    if serializer.is_valid() : 
        serializer.save()
    return Response(serializer.data)

   

