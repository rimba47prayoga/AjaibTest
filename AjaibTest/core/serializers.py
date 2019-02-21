from rest_framework import serializers

from .models import SimpleUser


class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpleUser
        fields = '__all__'
