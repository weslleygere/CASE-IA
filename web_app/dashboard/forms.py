from django import forms

class UploadFileForm(forms.Form):
    """
    A form class for uploading a file.

    Attributes:
        file (FileField): Field for uploading a file.

    """
    file = forms.FileField(label='Choose a file', help_text='File format should be .xls')