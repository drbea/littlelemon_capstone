from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

#app_name = "restaurant"

router = DefaultRouter()
# router.register(r"menu-item", views.MenuItemView, basename = "menu-item")
router.register(r"tables", views.BookingView)

urlpatterns = [
    path("booking/", include(router.urls)),

    path('menu/', views.MenuItemsView.as_view(), name = "menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    
    path("hello", views.sayHello),
    path("", views.index, name = "home"),
]


#add following lines to urlpatterns list 
