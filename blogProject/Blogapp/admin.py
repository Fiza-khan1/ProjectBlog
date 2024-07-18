from django.contrib import admin

from .models import PostModel,comments

class PostModeladmin(admin.ModelAdmin):
    list_display=('title','date_created')


admin.site.register(PostModel,PostModeladmin)
admin.site.register(comments)


