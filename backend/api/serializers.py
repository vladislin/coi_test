from rest_framework import serializers

from .models import Direction, Doctor


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class DoctorSerializer(serializers.ModelSerializer):
    directions = DirectionSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'slug', 'description', 'date_of_birth', 'experience', 'sort_num', 'directions')
        ordering = ['sort_num']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
