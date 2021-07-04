from rest_framework import serializers
from .models import Areas, Point


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields =  ['id' ,'lon', 'lat']

class AreaSerializer(serializers.ModelSerializer):
    points = PointSerializer()

    class Meta:
        model = Areas
        fields = ['id','name','description','points','fill_type','color1','color2','angle']

