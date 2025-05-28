from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Booking, Menu 

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ["id", "username", "uel", "email", "groups"]


class BookingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Booking
		fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = Menu
		fields = "__all__"


