from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.forms import UploadFileForm
from dashboard.views.file_upload import FileUploadView

class DashboardView(LoginRequiredMixin, View):
    """
    A view class for displaying the initial dashboard page.

    Attributes:
        login_url (str): The URL to redirect to if a user is not authenticated.
        file_upload_view (FileUploadView): An instance of the FileUploadView class.
    """
    login_url = '/login/'
    template_name = 'dashboard/dashboard.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_upload_view = FileUploadView()

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Renders the dashboard page.

        Args:
            request (HttpRequest): The request object used to generate this page.

        Returns:
            HttpResponse: The dashboard page.
        """
        user = request.user
        form = UploadFileForm()  # Initialize the file upload form

        context = {
            'user': user,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Handles form submissions on the dashboard.

        Args:
            request (HttpRequest): The request object used to generate this page.

        Returns:
            HttpResponse: The dashboard page or file upload page, depending on the form submitted.
        """
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if the file upload form is submitted
            if 'file' in request.FILES:
                # Delegate file upload logic to FileUploadView
                return self.file_upload_view.post(request)
        
        # Handle other form submissions or errors
        return self.get(request)

    def upload_file(self, request: HttpRequest) -> HttpResponse:
        """
        Handles file upload separately.

        Args:
            request (HttpRequest): The request object used to generate this page.

        Returns:
            HttpResponse: The file upload page.
        """
        # Delegate file upload logic to FileUploadView
        return self.file_upload_view.get(request)
