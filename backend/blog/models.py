from django.contrib.auth.models import User
from django.db import models


def image_upload_path(instance, filename):
    return f"posts/{instance.user.username}/{filename}"


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
