from django.shortcuts import render, redirect
from django.views import View
from user_management.forms import UserManagementForm
from user_management.utils import UserManagementUtils

class CreateUserView(View):
    """
    View for creating a new user.

    This view is responsible for handling requests to create a new user account.

    Attributes:
        template_name (str): The name of the template to be rendered.
    
    Methods:
        get: Handle GET requests to display the user creation form.
        post: Creates a new user.
    """    
    template_name = 'user_management/create_account.html'

    def get(self, request):
        """
        Handle GET requests to display the user creation form.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response containing the rendered form.

        """
        form = UserManagementForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        Creates a new user.

        Parameters:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The response object.
        """
        form = UserManagementForm(request.POST)
        context = {
            'form': form
        }

        if not form.is_valid():
            return render(request, self.template_name, context)
        
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        password_confirmation = form.cleaned_data['password_confirmation']

        user_management = UserManagementUtils(form, username, email, password, password_confirmation)

        if not user_management.validate_user_account():
            return render(request, self.template_name, context)
        
        user_management.create_user_account()

        return redirect('user_authentication:user_login')
        

        


        