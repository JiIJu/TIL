from rest_framework import serializers
from .models import Todo
from accounts.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ('id','user', 'title', 'is_completed',)

