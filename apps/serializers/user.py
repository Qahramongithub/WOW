from rest_framework import serializers

from apps.models import User


class UserSerializer(serializers.ModelSerializer):
    access = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username']