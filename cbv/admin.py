from django.contrib import admin
from .models import Post, Books




admin.site.register(Post)

@admin.register(Books)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}