from account.serializers import UserSerializer
from blog.models import BlogPost
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = BlogPost
        fields = "__all__"
