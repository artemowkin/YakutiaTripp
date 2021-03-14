from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""

    class Meta:
        model = Review
        fields = [
            'pk', 'name', 'avatar', 'rating', 'text', 'moderated', 'pub_date'
        ]
