from rest_framework import serializers

from posts.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'created_by',
            'uuid',
            'name',
            'description',
        )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'created_by',
            'created_at',
            'updated_at',
            'uuid',
            'name',
            'description',
            'likes_count',
            'dislikes_count'
        )
