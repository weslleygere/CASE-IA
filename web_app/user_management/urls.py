from django.urls import path
from .views.create_account import CreateUserView
from .views.edit_account import EditUserView
from .views.delete_account import DeleteUserView

app_name = 'user_management'

urlpatterns = [
    path('create_account/', CreateUserView.as_view(), name='create_account'),
    path('edit_account/<int:pk>/', EditUserView.as_view(), name='edit_account'),
    path('delete_account/<int:pk>/', DeleteUserView.as_view(), name='delete_account'),
]