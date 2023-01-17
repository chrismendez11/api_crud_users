from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser 


@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serialize = UserSerializer(users, many=True)

        return Response(serialize.data)
    elif request.method == 'POST':
        data = request.data
        serialize = UserSerializer(data=
        {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "email": data["email"],
            "password": make_password(data["password"]),
            "birthday": data["birthday"]
        })
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors)


@api_view(['PUT'])
def editUser(request, pk):
    data = request.data
    user = get_object_or_404(User, id=pk)
    serialize = UserSerializer(instance=user, data=data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)
    else:
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteUser(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return Response("User deleted successfully!")

