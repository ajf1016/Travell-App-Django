from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
import requests
import json

@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    name = request.data['name']
    email = request.data['email']
    password = request.data['password']
    
    if not User.objects.filter(username=email).exists():
        user =  User.objects.create_user(
            username=email,
            first_name = name,
            password = password
        )
        
        headers = {
            "Content-Type": "application/json"
        }
        
        # data = f'"username" : "{email}","password" : "{password}"'
        
        # final_data = "{" + data + "}"
        
        data = {
            "username" : email,
            "password" : password
        }
        
        protocol = "http://"
        if request.is_secure():
            protocol = "https://"
            
        host = request.get_host()
        
        url = protocol + host + "/api/v1/auth/token/"
        
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:  
            response_data = {
                "status_code" : 6000,
                "data" : response.json(),
                "message" : "Account Created successfully"  
            }
        else:
            response_data = {
                "status_code" : 6001,
                "data" : "An Error Occured"
            }
    else:
        response_data = {
            "status_code" : 6001,
            "data" : "This Account already registred"
        }
    
    return Response(response_data)