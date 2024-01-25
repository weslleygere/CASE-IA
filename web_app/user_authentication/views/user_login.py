from django.shortcuts import render, redirect
from django.views import View
from user_authentication.forms import UserLoginForm
from user_authentication.utils import UserAuthenticationUtils

class UserLoginView(View):
    """
    View for authenticating a user.

    This view is responsible for handling requests to authenticate a user.

    Attributes:
        template_name (str): The name of the template to be rendered.
    
    Methods:
        get: Handle GET requests to display the login form.
        post: Authenticates a user.
    """    
    template_name = 'user_authentication/user_login.html'

    def get(self, request):
        """
        Handle GET requests to display the login form.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response containing the rendered form.

        """
        form = UserLoginForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        Authenticates a user.

        Parameters:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The response object.
        """
        form = UserLoginForm(request.POST)
        context = {
            'form': form
        }

        if not form.is_valid():
            return render(request, self.template_name, context)
        
        username_or_email = form.cleaned_data['username_or_email']
        password = form.cleaned_data['password']

        user_authentication_utils = UserAuthenticationUtils(form, username_or_email, password)

        if not user_authentication_utils.authenticate_user():
            return render(request, self.template_name, context)
        
        user_authentication_utils.login_user(request)

        return redirect('dashboard:dashboard')