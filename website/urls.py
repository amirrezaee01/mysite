from django.urls import path
from website.views import *

app_name = "website"

urlpatterns = [
    path('',upgrade_view,name='upgrade'),
    
    path('',index_view,name='index'),
    path('about', about_view,name='about'), 
    path('contact', contact_view,name='contact'),
    path('newsletter',newsletter_view,name='newsletter'),

]

