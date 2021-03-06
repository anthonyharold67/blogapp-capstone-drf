from requests import Response
from rest_framework import serializers
from .models import Blog, Category, Comment, Like, PostView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"



class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    post_views = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'image', 'category', 'publish_date', 'author', 'status', 'slug', 'comments', 'likes','post_views')
    
    def create(self, validated_data):
        author = User.objects.get(username=self.context['request'].user)
        validated_data['author'] = author
        return Blog.objects.create(**validated_data)
    
    def get_likes(self, obj):
        return Like.objects.filter(post=obj).count()

    def get_post_views(self, obj):
        return PostView.objects.filter(post=obj).count()
    
        