from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogView(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = BlogPost.objects.all()
        cat = self.request.query_params.get("cat")
        if cat is not None:
            queryset = queryset.filter(category=cat)
        return queryset
