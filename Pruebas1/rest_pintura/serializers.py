from rest_framework import serializers
from core.models import Pinturas


class PinturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pinturas
        fields = ['id', 'nombre_pintura', 'precio_pintura', 'autor', 'categoria']
