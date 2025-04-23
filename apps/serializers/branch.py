from rest_framework import serializers

from apps.models import Branch


class BranchOneSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)


class BranchSerializer(serializers.Serializer):
    class Meta:
        model = Branch
        fields = '__all__'

