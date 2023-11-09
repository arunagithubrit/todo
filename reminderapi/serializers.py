from django.contrib.auth.models import User
from rest_framework import serializers
from reminder.models import Todos



class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","password","email"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    

class TodoSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    # status=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)

    class Meta:
        model=Todos
        fields="__all__"