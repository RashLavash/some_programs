from django.contrib import admin
from .models import Post, Tag, Review, Comments

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Comments)
