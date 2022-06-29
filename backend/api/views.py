from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Direction, Doctor
from .serializers import DirectionSerializer, DoctorSerializer
from .paginate import DoctorPagination


class DirectionViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    lookup_field = 'slug'


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all().prefetch_related('directions')
    serializer_class = DoctorSerializer
    lookup_field = 'slug'
    pagination_class = DoctorPagination
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['directions', 'experience']
    ordering = ['sort_num', 'name']
    ordering_fields = ['date_of_birth', 'experience']


