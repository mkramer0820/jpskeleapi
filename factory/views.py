from rest_framework import generics

from .serializers import FactoryListSerializer
from .serializers import Factory


class FactoryCreateView(generics.ListCreateAPIView):

    queryset = Factory.objects.all()
    serializer_class = FactoryListSerializer


class FactoryDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Factory.objects.all()
    serializer_class = FactoryListSerializer