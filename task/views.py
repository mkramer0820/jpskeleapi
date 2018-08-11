from rest_framework import generics
from .serializers import TaskModelSerializer, SerializerMethodField


from task.models import SampleTaskBasic

class TaskCreateView(generics.ListCreateAPIView):

    queryset = SampleTaskBasic.objects.all()
    serializer_class = TaskModelSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = SampleTaskBasic.objects.all()
    serializer_class = TaskModelSerializer