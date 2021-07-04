from django.urls import path, include
from rest_framework import routers
from . import views
# from .views import AreaViewSet
from .views import AreasViewSet

router = routers.DefaultRouter()
router.register('areas', AreasViewSet, basename='Areas')


urlpatterns = [
    path('', include(router.urls)),
]