from django import forms

class UserLoginForm(forms.Form):
    """
    A class used to represent a user login form, containing the username and password fields.

    Attributes:
        username_or_email (CharField): Field for entering the username or email address.
        password (CharField): Field for entering the password.
    """
    username_or_email = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nome de usuário ou e-mail'
            }
        )
    )

    password = forms.CharField(
        max_length=32, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Senha'
            }
        )
    )