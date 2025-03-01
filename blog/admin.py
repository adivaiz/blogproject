from django.contrib import admin
from .models import Post,Author,Tag,Comment


class PostAdmin(admin.ModelAdmin):
    list_filter=("author","tags","date",) #to filter in the admin page by
    list_display=("title","date","author",)
    prepopulated_fields={"slug":("title",)} #for auto fill field
class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","post")
admin.site.register(Post,PostAdmin) # we pass the class and the admin func to sort
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)