from django.shortcuts import render

from rest_framework.views import APIView
from django.http import JsonResponse
import requests

from rest_framework import status


''' 
   We are using 2factor api for otp verification.
    for more info about please goto https://www.2factor.in
'''
class sendOTPView(APIView):
    def post(self, request):
        if request.method == "POST":
            phone_number = request.POST["ph_num"]

            api_key = "f79adac9-1711-11ea-9fa5-0200cd936042" # an unique api key to get authorization
                                                            # to access 2factor api

            url = "http://2factor.in/API/V1/"+ api_key+ "/SMS/" + phone_number +"/AUTOGEN/OTPSEND"
            print(url)
            try:
                response = requests.request("GET", url)
                message =  {"status": "Sucessfully otp has generated"}
            except:
                message = {"status" : "OTP generation failed"}
                return JsonResponse(message, status=status.HTTP_404_NOT_FOUND)
            data = response.json()
            print(data)
            request.session["otp_details"] = data["Details"]   # OTP data is stored in session for further verification
            return JsonResponse(message, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse("Only post method is allowed", safe=False, status=status.HTTP_405_METHOD_NOT_ALLOWED)



            

