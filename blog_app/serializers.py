from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(max_length=255, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
