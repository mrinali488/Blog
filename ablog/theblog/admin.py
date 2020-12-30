from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ("created_on", "author")
    search_fields = ['title', 'content', 'author']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)