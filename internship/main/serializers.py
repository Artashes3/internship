from rest_framework import serializers
from . models import *


class SerilizeUser(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields  = ["username","email","password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password",None)
        obj = self.Meta.model(**validated_data)
        if password:
            obj.set_password(password)
        obj.save()
        return obj
    
    
        
class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","text"]

