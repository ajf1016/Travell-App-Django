from rest_framework.serializers import ModelSerializer
from places.models import Place,Gallery
from rest_framework import serializers 


class PlaceSerializer(ModelSerializer):
    class Meta:
        fields = ('id',"name","featured_image","place")
        model = Place
        
        
class GallerySerializer(ModelSerializer):
    class Meta:
        fields = ('id',"image")
        model = Gallery
        

class PlaceDetailSerializer(ModelSerializer):
    category = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()
    class Meta:
        fields = ('id',"name","featured_image","place","category","description","gallery")
        model = Place
    
    def get_category(self,instance):
        return instance.category.name
    
    def get_gallery(self,instance):
        request = self.context.get("request")
        images = Gallery.objects.filter(place=instance)
        serializer = GallerySerializer(images,many=True,context={"request" : request})
        
        return serializer.data
        