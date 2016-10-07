from rest_framework import serializers

from . import models


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Review

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'desc',
            'created_at',
        )
        model = models.Course