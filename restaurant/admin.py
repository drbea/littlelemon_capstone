from django.contrib import admin

# Register your models here.
from . models import Booking, Menu


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	pass