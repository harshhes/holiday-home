from django.urls import path, include
from .views import RegisterOwnerView, LoginView
from .routers import router 

urlpatterns = [
    path('register', RegisterOwnerView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    
    path('hh/', include(router.urls))
]