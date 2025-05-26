from django.urls import path

from . import views

urlpatterns = [
    path("hello", views.sayHello),
    path("", views.index, name = "home"),
]
