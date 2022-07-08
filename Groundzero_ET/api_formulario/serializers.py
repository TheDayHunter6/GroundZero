from rest_framework import serializers
from core.models import Contacto, Pinturas


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'
