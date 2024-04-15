from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = fields = ['id', 'text', 'created_date', 'post', 'author']
        read_only_fields = ['author', 'likes'] 

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user 
        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'published_date', 'likes', 'comments']
        read_only_fields = ['author', 'published_date', 'likes'] 

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user  
        return super().create(validated_data)


