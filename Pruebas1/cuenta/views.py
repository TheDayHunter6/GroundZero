from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cuenta.serializers import SerializerRegistro
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

# Create your views here.

#no funciona
@api_view(['POST',])
def registro_view(request):
    data = {}
    
    serializer = SerializerRegistro(data=request.data)
    if serializer.is_valid():
        User = serializer.save()
        data['response'] = "se registrado correctamente"
        data['username'] = User.username
        data['email'] = User.email
    else:
        data = serializer.errors
    return Response(data)

@api_view(['POST'])
def login1(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario Inválido')
    sw = check_password(password, user.password)
    if not sw:
        return Response('Password inválida')
    
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)