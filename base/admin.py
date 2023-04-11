from django.contrib import admin
from .models import *


@admin.register(Owner)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name', 'username','created_on']
   
    search_fields = ['email']


@admin.register(HolidayHome)
class HHAdmin(admin.ModelAdmin):
    list_display = ['name','city']
   
    search_fields = ['name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_no','is_available', 'holiday_home',]
   
    search_fields = ['room_no']