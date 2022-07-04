from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Pinturas
from .serializers import PinturasSerializer
from django.contrib.auth.models import User
from core.models import Pinturas
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes((IsAuthenticated))
@api_view(['GET'])
def lista_pintura(request, id):
    """
    Lista de pinturas
    """
    try:
        Pinturas = Pinturas.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PinturasSerializer(Pinturas)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_pintura(request, id):
    """
    Get, update o delete de una pintura en particular
    """
    try:
        Pinturas = Pinturas.objects.get(idPintura=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PinturasSerializer(Pinturas)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PinturasSerializer(Pinturas, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Pinturas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
