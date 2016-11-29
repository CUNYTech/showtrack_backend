from rest_framework import serializers

from . import models


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Review

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'show_id',
            'progress',
            'last_updated',
            'created_at'
            
        )
        model = models.WatchList

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'content',
            'last_updated',
            'created'
        )
        model = models.Show