from rest_framework import serializers

from . import models


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Review

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'created_at',
            'show_id',
            'progress',
            'user'
        )
        model = models.WatchList