from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Areas, Point
from .serializer import AreaSerializer, PointSerializer


class AreasViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer

    def get_queryset(self):
        areas = Areas.objects.all()
        return areas

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_points = Point.objects.create(lon= post_data['points']['lon'], lat=post_data['points']['lat'])
        new_points.save

        new_area = Areas.objects.create(name = post_data['name'],description = post_data['description'],points = new_points,
                                        fill_type = post_data['fill_type'],color1 = post_data['color1'],color2 = post_data['color2'],
                                        angle = post_data['angle'],)
        new_area.save()

        serializer = AreaSerializer(new_area)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        area_objecs = self.get_object()
        post_data = request.data

        area_objecs.name = post_data['name']
        area_objecs.description = post_data['description']
        area_objecs.fill_type = post_data['fill_type']
        area_objecs.color1 = post_data['color1']
        area_objecs.color2 = post_data['color2']
        area_objecs.angle = post_data['angle']

        area_objecs.save()
        serializer = AreaSerializer()

        return Response('Updated succesfully')








        return Response(serializer.data)



