from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class UserLogoutView(LoginRequiredMixin, View):
    """
    A view class for handling user logout.

    Attributes:
        login_url (str): The URL to redirect to if a user is not authenticated.
    """

    login_url = '/login/'

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Handles GET requests for user logout.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A response object that logs the user out and redirects to the login page.
        """
        logout(request)
        return redirect('user_authentication:user_login')
    