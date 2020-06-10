from django.contrib import admin

# Register your models here.
from blog.models import Post
from blog.models import BlogComment
admin.site.register((BlogComment,Post))