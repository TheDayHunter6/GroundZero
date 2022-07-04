
from dataclasses import fields
import email
from rest_framework import serializers
from django.contrib.auth.models import User 

class SerializerRegistro(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]
        extra_kwargs = { 'password': {'write_only': True}}
    
    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
        password = self.validated_data['password']
        

       
        User.set_password(password)
        User.save()
        return user

    