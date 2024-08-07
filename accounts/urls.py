from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
     path('password_reset/', forget_password_view, name='password_reset'),
    path('reset_password/<int:user_id>/', reset_password_view, name='reset_password'),
]