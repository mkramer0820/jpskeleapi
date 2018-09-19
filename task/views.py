from rest_framework import generics
from .serializers import TaskModelSerializer, SerializerMethodField


from task.models import CostcoSampleTasks

class TaskCreateView(generics.ListCreateAPIView):

    queryset = CostcoSampleTasks.objects.all()
    serializer_class = TaskModelSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CostcoSampleTasks.objects.all()
    serializer_class = TaskModelSerializer