from django.urls import path

from .views import sendOTPView

urlpatterns = [
    path('send-otp/', sendOTPView.as_view()),

]
