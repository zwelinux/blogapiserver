from rest_framework import serializers

from .models import Post
from django.contrib.auth.models import Group, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'link', 'link_name', 'content', 'date_posted', 'author')
        # fields = ('title', 'date_posted', 'author')