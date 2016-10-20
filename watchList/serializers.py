from rest_framework import serializers

from . import models


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Review

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'desc',
            'created_at',
            'shows',
            'user'
        )
        model = models.WatchList