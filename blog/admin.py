from django.contrib import admin
from .models import Post, Baiviet, Project, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Baiviet)
admin.site.register(Project)
