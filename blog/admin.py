from django.contrib import admin
from blog.models import Post, Catagory, Comment  

class PostAdmin(admin.ModelAdmin):  
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'login_require', 'published_date')
    list_filter = ('status', 'author')
    # ordering = ['created_date']
    search_fields = ['title', 'content']
    # Removed summernote_fields configuration

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Catagory)  
admin.site.register(Post, PostAdmin)
