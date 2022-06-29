from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DirectionViewSet, DoctorViewSet


api_router = DefaultRouter()
api_router.register('directions', DirectionViewSet, 'directions')
api_router.register('doctors', DoctorViewSet, 'doctors')

urlpatterns = [
    path('api/', include(api_router.urls))
]