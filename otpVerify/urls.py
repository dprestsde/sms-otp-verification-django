from django.urls import path

from .views import sendOTPView, verifyOTPView

urlpatterns = [
    path('send-otp/', sendOTPView.as_view()),
    path('verify-otp/', verifyOTPView.as_view())

]
