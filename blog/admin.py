from django.contrib import admin
from .models import Post, Comment
admin.site.site_header = "tweetie Admin"
admin.site.site_title = "tweetie Admin Panel"
admin.site.index_title = "Welcome to tweetie Admin Panel"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ['date_posted']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
