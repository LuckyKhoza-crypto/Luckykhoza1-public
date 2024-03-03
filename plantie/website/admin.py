from django.contrib import admin
from .models import PostImage, Tree
# Register your models here.

class PostImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(PostImage, PostImageAdmin)

admin.site.register(Tree)