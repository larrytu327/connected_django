from django.contrib import admin
from .models import MessageBoard, UserProfile, Post

admin.site.register(MessageBoard)
admin.site.register(UserProfile)
admin.site.register(Post)