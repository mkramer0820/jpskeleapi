from rest_framework import serializers
from todos.models import TodosGroup, Todos

class TodosGroupSerializer(serializers.ModelSerializer):


    class Meta:
        model = TodosGroup
        fields = '__all__'


class TodosSerializer(serializers.ModelSerializer):

    todos = serializers.JSONField
    group = serializers.ReadOnlyField(source='todos_group.name')

    class Meta:
        model = Todos
        fields = '__all__'
