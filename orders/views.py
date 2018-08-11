
from rest_framework import generics

from .serializers import OrderlistSerializer
from .serializers import Orders


class OrderCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Orders.objects.all()
    serializer_class = OrderlistSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Orders.objects.all()
    serializer_class = OrderlistSerializer