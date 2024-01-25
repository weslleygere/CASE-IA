from django.contrib.auth.models import User
from django.contrib.auth import login

class UserAuthenticationUtils:
    """
    A class for performing user authentication validations.

    Attributes:
        form (UserAuthenticationForm): The form containing the user authentication data.
        username_or_email (str): The username or email address to be validated.
        password (str): The password to be validated.

    """

    def __init__(self, form, username_or_email, password):
        """
        Initialize the UserAuthenticationUtils class.

        Args:
            form (UserAuthenticationForm): The form containing the user authentication data.
            username_or_email (str): The username or email address to be validated.
            password (str): The password to be validated.

        """
        
        self.form = form
        self.username_or_email = username_or_email.lower()
        self.password = password

    def username_or_email_exists(self, username_or_email) -> bool:
        """
        Check if the given username or email address already exists in the database.

        Args:
            username_or_email (str): The username or email address to be validated.

        Returns:
            bool: True if the username or email address exists, False otherwise.

        """
        return User.objects.filter(username=username_or_email).exists() or User.objects.filter(email=username_or_email).exists()
    
    def check_password(self, username_or_email, password) -> bool:
        """
        Check if the given password is valid.

        Args:
            username_or_email (str): The username or email address to be validated.
            password (str): The password to be validated.

        Returns:
            bool: True if the password is valid, False otherwise.

        """
        user = User.objects.filter(username=username_or_email).first() or User.objects.filter(email=username_or_email).first()
        return user.check_password(password)
    
    def authenticate_user(self) -> bool:
        """
        Authenticate the user.

        Returns:
            bool: True if the user was authenticated, False otherwise.

        """
        if not self.username_or_email_exists(self.username_or_email):
            self.form.add_error('username_or_email', 'O nome de usuário ou e-mail informado não existe.')
            return False
        
        if not self.check_password(self.username_or_email, self.password):
            self.form.add_error('password', 'A senha informada está incorreta.')
            return False
        
        return True
        

    def login_user(self, request) -> None:
        """
        Log in the user.

        Args:
            request (HttpRequest): The request object.

        """
        user = User.objects.filter(username=self.username_or_email).first() or User.objects.filter(email=self.username_or_email).first()
        login(request, user)

