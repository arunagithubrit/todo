from task.models import Todos
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    due_date=serializers.CharField(read_only=True)
    
    class Meta:
        model=Todos
        fields="__all__"
