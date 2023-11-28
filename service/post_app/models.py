from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """post models"""
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)

    likes = models.PositiveIntegerField(default=0, blank=True)
    views = models.PositiveIntegerField(default=0, blank=True)

    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')

    def __str__(self) -> str:
        return f'Post: {self.title}'
    

class Comment(models.Model):
    """commentary model"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=256)

    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    likes = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self) -> str:
        return f'Comment: {self.owner}'


class UserPostRelations(models.Model):
    """user post relation"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viewer')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    is_liked = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    is_viewed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user} : {self.post}'


class UserCommentRelations(models.Model):
    """user comment relation"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user} : {self.comment}'

