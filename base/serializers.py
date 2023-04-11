from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import HolidayHome, Owner, Room
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class RegisterOwnerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset = Owner.objects.all())])

    password = serializers.CharField(write_only =True,required=True, validators=[validate_password], style ={'input_type': 'password'})

    confirm_password = serializers.CharField(write_only=True, required=True, style ={'input_type': 'password'})

    class Meta:
        model = Owner
        fields = ('id', 'first_name', 'last_name','email', 'username','password', 'confirm_password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':{"Password fields didn't match"}})

        return attrs

    def create(self, validated_data):
        user = Owner.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username']
            )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Owner
        fields= ['email', 'password']



class HolidayHomeSerializer(serializers.ModelSerializer):

    class Meta:
        # exclude = []
        fields = ['id', 'name', 'address', 'phone', 'city', 'rooms', 'owners']
        model = HolidayHome
        depth = 1


class HolidayRoomSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = []
        model = Room
        depth = 2
    