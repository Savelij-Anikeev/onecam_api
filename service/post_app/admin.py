from django.contrib import admin
from .models import Post, Comment, UserPostRelations, UserCommentRelations


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserPostRelations)
admin.site.register(UserCommentRelations)
