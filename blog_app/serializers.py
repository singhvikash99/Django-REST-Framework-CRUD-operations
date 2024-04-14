from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'published_date', 'likes']
        read_only_fields = ['author', 'published_date', 'likes'] 

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user  
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author'] 

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user 
        return super().create(validated_data)
