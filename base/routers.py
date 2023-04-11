from rest_framework.routers import DefaultRouter
from .views import * 

router = DefaultRouter()

router.register('holiday-home', HolidayHomeViewset, basename='holiday-home')
router.register('holiday-room', HolidayRoomViewset, basename='holiday-room')