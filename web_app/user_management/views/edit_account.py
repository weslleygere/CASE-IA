from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from user_management.forms import EditUserManagementForm

class EditUserView(View):
    """
    A class used to represent a view for editing a user.

    Attributes:
        template_name (str): Path to the HTML template.
    """
    template_name = 'user_management/edit_account.html'

    def get(self, request, pk):
        """
        Renders the edit account page.

        Args:
            request (HttpRequest): The request object used to generate this page.
            pk (int): The primary key of the user to be edited.

        Returns:
            HttpResponse: The edit account page.
        """
        user = User.objects.get(id=pk)
        form = EditUserManagementForm(initial={
            'username': user.username,
            'email': user.email
        })
        context = {
            'form': form,
            'pk': pk
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        """
        Updates a user in the database.

        Args:
            request (HttpRequest): The request object used to generate this page.
            pk (int): The primary key of the user to be edited.

        Returns:
            HttpResponseRedirect: Redirects the user to the homepage.
        """

        user = User.objects.get(id=pk)
        form = EditUserManagementForm(request.POST, initial={'username': user.username, 'email': user.email})
        context = {
            'form': form,
            'pk': pk,
        }

        if not form.is_valid():
            return render(request, self.template_name, context)
        
        user.username = form.cleaned_data['username']
        user.email = form.cleaned_data['email']

        if User.objects.filter(username=user.username).exclude(pk=user.pk).exists():
            form.add_error('username', 'Nome de usuário já cadastrado.')
            return render(request, self.template_name, context)

        if User.objects.filter(email=user.email).exclude(pk=user.pk).exists():
            form.add_error('email', 'E-mail já cadastrado.')
            return render(request, self.template_name, context)
        
        if form.cleaned_data.get('password'):
            user.set_password(form.cleaned_data['password'])

        user.save()

        return redirect('dashboard:dashboard')

    
