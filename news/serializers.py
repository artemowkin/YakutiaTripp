from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    """Serializer for News model"""

    class Meta:
        model = News
        fields = ['title', 'preview', 'text', 'pub_date']
        read_only_fields = ['pub_date']
