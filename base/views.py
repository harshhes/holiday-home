from rest_framework import generics, viewsets, permissions
from .serializers import *
from rest_framework.decorators import action
from .models import *
from django.contrib.auth import login
from utility.response_handler import HTTPResponse
from rest_framework_simplejwt.tokens import RefreshToken

# generate JWT token after login
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


#authenticate user via email
def authenticate_user(email, password):
    try:
        owner = Owner.objects.get(email=email)
    except Owner.DoesNotExist:
        return None
    if owner.check_password(password):
        return owner



class RegisterOwnerView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = RegisterOwnerSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, format=None):

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email') 
            password = serializer.data.get('password') 

            user = authenticate_user(email=email, password=password)
            
            if user is not None:
                token = get_tokens_for_user(user)
                login(request,user)
                data = {'msg':"Login Success!", 'token':token}
                return HTTPResponse(status_code=200).generic_response(data=data)
            else:
                return HTTPResponse(status_code=404).generic_response(data="email or password is not valid!!")

        return HTTPResponse(status_code=400).generic_response(data=serializer.errors)


# hh/holiday-home/

class HolidayHomeViewset(viewsets.ModelViewSet):
    queryset = HolidayHome.objects.all()
    serializer_class = HolidayHomeSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    @action(detail=True, methods=['get'])  
    def get_owners_to_hh(self, request, pk=None):
        data = request.data
        # pk = pk
        owners = HolidayHome.objects.filter(id=pk)
        serializer = HolidayHomeSerializer(owners, many=True)
        data= serializer.data

        return HTTPResponse(status_code=200).generic_response(data=data)

class HolidayRoomViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = HolidayRoomSerializer
    permission_classes = [permissions.IsAuthenticated]
