from rest_framework import serializers
from factory.models import Factory


class FactoryListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Factory
        fields = '__all__'
