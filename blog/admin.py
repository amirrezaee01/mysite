from django.contrib import admin
from blog.models import Post,Catagory
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ('title','author','counted_views','status','published_date')
    list_filter = ('status','author') 
    #ordering = ['created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)

admin.site.register(Catagory)
admin.site.register(Post,PostAdmin)
