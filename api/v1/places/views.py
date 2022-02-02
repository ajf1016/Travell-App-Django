from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from api.v1.places.serializer import PlaceSerializer,PlaceDetailSerializer
from places.models import Place


@api_view(["GET"])
@permission_classes([AllowAny])
def places(request):
    instance = Place.objects.filter(is_deleted=False)
    serializer = PlaceSerializer(instance,many=True,context={"request" : request},)
    reponse_data = {
        "status_code" : 6000,
        "data" : serializer.data
    }
    return Response(reponse_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def place(request,pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.filter(is_deleted=False)
        serializer = PlaceDetailSerializer(instance,many=True,context={"request" : request},)
        reponse_data = {
            "status_code" : 6000,
            "data" : serializer.data
        }
        return Response(reponse_data)
    else:
        reponse_data = {
            "status_code" : 6001,
            "message" : "Place not exist"
        }
        return Response(reponse_data)
    
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected(request,pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.filter(is_deleted=False)
        serializer = PlaceDetailSerializer(instance,many=True,context={"request" : request},)
        reponse_data = {
            "status_code" : 6000,
            "data" : serializer.data
        }
        return Response(reponse_data)
    else:
        reponse_data = {
            "status_code" : 6001,
            "message" : "Place not exist"
        }
        return Response(reponse_data)