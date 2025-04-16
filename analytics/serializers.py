from rest_framework import serializers
from .models import UserCreation

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreation
        fields = ['user_id', 'user_name', 'user_updated_date', 'user_updated_time']

