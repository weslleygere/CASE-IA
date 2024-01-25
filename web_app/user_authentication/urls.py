from django.urls import path
from user_authentication.views.user_login import UserLoginView
from user_authentication.views.user_logout import UserLogoutView

app_name = 'user_authentication'

urlpatterns = [
    path('', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]