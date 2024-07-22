from django.contrib import admin
from website.models import Contact

class ContatcAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','subject')
    list_filter = ['email']
    search_fields = ('name','massage')
    

admin.site.register(Contact,ContatcAdmin)