
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from task.models import CostcoSampleTasks
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField, SerializerMethodField
from django.shortcuts import get_object_or_404, redirect
from orders.models import Orders


class TaskModelSerializer(serializers.ModelSerializer):

    order = PrimaryKeyRelatedField(queryset=Orders.objects.all())
    style_number = serializers.ReadOnlyField()

    class Meta:
        model = CostcoSampleTasks
        fields = "__all__"


class TaskListSerializer(serializers.Serializer):

    order = serializers.StringRelatedField()

    class Meta:

        model = CostcoSampleTasks
        fields = '__all__'

@permission_classes((permissions.AllowAny,))
class TemplateTaskList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task_list.html'



    def get(self, request):

        task_list = CostcoSampleTasks.objects.all()
        serializers = TaskListSerializer(task_list, data=request.data)

        return Response({'serializer':serializers, 'task_list':task_list})

    def post(self, request, pk):
        task = get_object_or_404(CostcoSampleTasks, pk=pk)
        serializer = TaskListSerializer(task, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'task_detail': task})
        serializer.save()
        return redirect('profile-list')


class TaskView(generics.ListAPIView):

    queryset = CostcoSampleTasks.objects.all()
    serializer_class = TaskListSerializer

    def perform_create(self, serializer):

        serializer.save()