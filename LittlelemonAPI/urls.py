from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
# app_name = "LittlelemonAPI"

urlpatterns = [
	path("menu-items", views.MenuItemsView.as_view(), name = "menu-items"),
	path("menu-items/<int:pk>", views.SingleMenuItemView.as_view(), name = "menu-items"),
	path("message", views.msg, name = "protect-msg"),
	path("token-auth", obtain_auth_token),

]