from rest_framework import serializers

from .models import TourDay, Tour


class TourDaySerializer(serializers.ModelSerializer):
    """Serializer for TourDay model"""

    class Meta:
        model = TourDay
        fields = ['weekday', 'description']


class TourSerializer(serializers.ModelSerializer):
    """Serializer for Tour model"""
    days = TourDaySerializer(many=True)

    class Meta:
        model = Tour
        fields = [
            'pk', 'title', 'preview', 'short_description', 'days', 'about',
            'price', 'city_from', 'city_to', 'views'
        ]
        read_only_fields = ['pk', 'views']
