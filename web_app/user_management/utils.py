from django.contrib.auth.models import User

class UserManagementUtils:
    """
    A class for performing user account validations.

    Attributes:
        form (UserManagementForm): The form containing the user account data.
        username (str): The username to be validated.
        email (str): The email address to be validated.
        password (str): The password to be validated.
        password_confirmation (str): The password confirmation to be validated.

    """

    def __init__(self, form, username, email, password, password_confirmation):
        """
        Initialize the UserManagementUtils class.

        Args:
            form (UserManagementForm): The form containing the user account data.
            username (str): The username to be validated.
            email (str): The email address to be validated.
            password (str): The password to be validated.
            password_confirmation (str): The password confirmation to be validated.

        """
        
        self.form = form
        self.username = username.lower()
        self.email = email
        self.password = password
        self.password_confirmation = password_confirmation

    def username_exists(self, username) -> bool:
        """
        Check if the given username already exists in the database.

        Args:
            username (str): The username to be validated.

        Returns:
            bool: True if the username exists, False otherwise.

        """
        return User.objects.filter(username=username).exists()

    def email_exists(self, email) -> bool:
        """
        Check if the given email address already exists in the database.

        Args:
            email (str): The email address to be validated.

        Returns:
            bool: True if the email address exists, False otherwise.

        """
        return User.objects.filter(email=email).exists()
    
    def check_matching_passwords(self, password, password_confirmation) -> bool:
        """
        Check if the given passwords match.

        Args:
            password (str): The password to be validated.
            password_confirmation (str): The password confirmation to be validated.

        Returns:
            bool: True if the passwords match, False otherwise.

        """
        return password == password_confirmation
    
    def validate_user_account(self) -> bool:
        """
        Validate the user account.

        This method performs a series of validations on the user account data
        and adds the appropriate error messages to the form if any of the
        validations fail.

        Returns:
            bool: True if the user account is valid, False otherwise.

        """
        if self.username_exists(self.username):
            self.form.add_error('username', 'O nome de usuário já existe.')
            return False

        if self.email_exists(self.email):
            self.form.add_error('email', 'O e-mail já existe.')
            return False

        if not self.check_matching_passwords(self.password, self.password_confirmation):
            self.form.add_error('password_confirmation', 'As senhas não conferem.')
            return False

        return True
    
    def create_user_account(self) -> User:
        """
        Create a new user.

        Returns:
            User: The newly created user.

        """
        user = User.objects.create_user(
            username=self.username, 
            email=self.email
        )
        user.set_password(self.password)
        user.save()

        return user