
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status

from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from customer.serializers import CustomerSerializer
from rest_framework import viewsets



from .serializers import OrderlistSerializer, OrderlistNameSerializer, OrderFileSerializer
from .serializers import Orders


class OrderCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Orders.objects.all()
    serializer_class = OrderlistSerializer



class OrderCreateNamesView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Orders.objects.all()
    serializer_class = OrderlistNameSerializer



class OrderFileView(APIView):

  parser_classes = (MultiPartParser, FormParser, JSONParser)

  def post(self, request, *args, **kwargs):
    file_serializer = OrderFileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
test view for orders
"""

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Orders.objects.all()
    serializer_class = OrderlistSerializer

