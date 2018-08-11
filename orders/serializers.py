from rest_framework import serializers
from orders.models import Orders


class OrderlistSerializer(serializers.ModelSerializer):

    buyer = serializers.StringRelatedField()

    class Meta:
        model = Orders
        fields = '__all__'
        #fields = ('tasks',)
