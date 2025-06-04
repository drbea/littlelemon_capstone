from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view

from .models import Booking, Menu
from . serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
def sayHello(request):
    return HttpResponse("Hello world")

def index(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]



class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]