# from django.shortcuts import render

from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.decorators import api_view, permission_classes

from restaurant.serializers import MenuItemSerializer, BookingSerializer
from restaurant.models import Menu 
# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
#    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
	data = {"message": "This message need authentication to be view "}
	return Response(data)
