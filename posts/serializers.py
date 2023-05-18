from rest_framework import serializers
from posts.models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Validation check for size, width and height on post images
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
                )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
                )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Gets current user and check if authenticated.
        Check if logged in user likes any posts by
        filtering Like object.
        If yes the post instance is returned.
        Return none if user is not authenticated or does not like a post
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'country', 'location',
            'difficulty', 'rating', 'image_filter', 'like_id'
        ]
