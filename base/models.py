from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager



class Owner(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(null=True)
    homes = models.ForeignKey('HolidayHome', on_delete=models.CASCADE, null=True, blank=True, related_name='owners')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        default_permissions = ('add', 'view', 'change', 'delete')



class HolidayHome(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_no = models.CharField(max_length=10)
    holiday_home = models.ForeignKey(HolidayHome, on_delete=models.CASCADE, null=True, blank=True, related_name='rooms')
    is_available = models.BooleanField(default=True)
    rules_of_the_house = models.TextField()

    def __str__(self):
        return self.room_no


