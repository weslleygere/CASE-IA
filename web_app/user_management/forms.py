from django import forms

class UserManagementForm(forms.Form):
    """
    A class used to represent a user management, containing the username, 
    email address, password and password confirmation fields.

    Attributes:
        username (CharField): Field for entering the new username.
        email (EmailField): Field for entering the new email address.
        password (CharField): Field for entering the new password.
        password_confirmation (CharField): Field for confirming the new password.
    """
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nome de usuário'
            }
        )
    )

    email = forms.EmailField(
        max_length=100, 
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'E-mail'
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

    password_confirmation = forms.CharField(
        max_length=32, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmação de Senha'
            }
        )
    )


class EditUserManagementForm(forms.Form):
    """
    A class used to represent a user management, containing the username, 
    email address, password and password confirmation fields.

    Attributes:
        username (CharField): Field for entering the new username.
        email (EmailField): Field for entering the new email address.
        password (CharField): Field for entering the new password.
        password_confirmation (CharField): Field for confirming the new password.
    """
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nome de usuário'
            }
        )
    )

    email = forms.EmailField(
        max_length=100, 
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'E-mail'
            }
        )
    )

    password = forms.CharField(
        max_length=32, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Nova Senha (Opcional)'
            }
        ),
        required=False  # Make the password field optional
    )

    password_confirmation = forms.CharField(
        max_length=32, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmação de Senha'
            }
        ),
        required=False  # Make the password confirmation field optional
    )                                                                                              
