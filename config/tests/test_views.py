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

        res = self.client.get(reverse("LittlelemonAPI:menu-items"))
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many = True)

        print(f"\n\n res: {res}\n menus:{menus}\n serializer: {serializer}")
        self.assertEqual(res.status_code, 200)
#        self.assertContains(res.data, serializer.data)


if __name__ == "__main__":
    MenuViewTest.test_getall()
