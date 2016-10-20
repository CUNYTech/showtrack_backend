from rest_framework import serializers

from django.contrib.auth import get_user_model


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Review

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'display_name',
            'password',
        )
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, data):
        email = data["email"]
        username = data["username"]
        display_name = data["display_name"]
        password = data["password"]

        user = User(
            email = email,
            username = username,
            display_name = display_name
        )
        user.set_password(password)
        user.save()
        return data
