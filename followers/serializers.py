from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    Create method handles the unique constraint on 'owner' and 'followed'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'followed', 'followed_name', 'created_at'
        ]

    def create(self, validated_data):
        """
        Allows user to follow a profile
        Returns a complete pbject instance if data is valid
        Handles duplicate follows.
        Throws interity error if user already follows a profile
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
