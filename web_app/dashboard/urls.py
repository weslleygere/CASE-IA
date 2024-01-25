from django.urls import path
from dashboard.views.dashboard import DashboardView
from dashboard.views.file_upload import FileUploadView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('upload/', FileUploadView.as_view(), name='file_upload')
]