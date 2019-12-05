from django.shortcuts import render

from rest_framework.views import APIView
from django.http import JsonResponse
import requests

from rest_framework import status


''' 
   We are using 2factor api for otp verification.
    for more info about please goto https://www.2factor.in
'''

api_key = "f79adac9-1711-11ea-9fa5-0200cd936042" # an unique api key to get authorization
                                                            # to access 2factor api
class sendOTPView(APIView):
    def post(self, request):
        if request.method == "POST":
            phone_number = request.POST["ph_num"]

            url = "http://2factor.in/API/V1/"+ api_key+ "/SMS/" + phone_number +"/AUTOGEN/OTPSEND"
            try:
                response = requests.request("GET", url)
                
            except:
                message = {"status" : "OTP generation failed"}
                return JsonResponse(message, status=status.HTTP_404_NOT_FOUND)
            data = response.json()
            print(data)
            request.session["otp_details"] = data["Details"]   # OTP data is stored in session for further verification
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse("Only post method is allowed", safe=False, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class verifyOTPView(APIView):
    def post(self, request):
        if request.method == "POST":
            user_otp = request.POST["otp"]
            print(user_otp)
            url = "http://2factor.in/API/V1/"+ api_key  +  "/SMS/VERIFY/" + request.session['otp_details'] + "/" + user_otp + ""
            print(url)
            response = requests.request("GET", url)		
            print(response)
            data = response.json()
            print(data)
            if data['Status'] == "Success":
                return JsonResponse(data, status=status.HTTP_202_ACCEPTED)
            else:
                return JsonResponse(data, status=status.HTTP_401_UNAUTHORIZED)
	    
        else:
            return JsonResponse(response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

