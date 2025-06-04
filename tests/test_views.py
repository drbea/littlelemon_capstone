from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from restaurant.serializers import MenuItemSerializer
from restaurant.models import Menu

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title = "IceCream", price = 90, inventory = 100)
        Menu.objects.create(title = "Pizza", price = 120, inventory = 50)
        Menu.objects.create(title = "Salad", price = 37, inventory = 30)

    def test_getall(self):
        client = APIClient()

        res = self.client.get(reverse("menu"))
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many = True)

        print(f"\n\n res: {res}\n menus:{menus}\n serializer: {serializer}")
        # self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)


