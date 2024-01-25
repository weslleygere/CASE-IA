from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.models import User

class DeleteUserView(View):
    """
    A class used to represent a view for deleting a user.
    """
    def get(self, request, pk):
        """
        Deletes a user from the database.

        Args:
            request (HttpRequest): The request object used to generate this page.
            pk (int): The primary key of the user to be deleted.

        Returns:
            HttpResponseRedirect: Redirects the user to the homepage.
        """

        user = User.objects.get(id=pk)
        user.delete()
    
        return redirect('dashboard:dashboard')