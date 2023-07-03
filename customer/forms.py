from django import forms
from .models import Customer


# Form for merchant registration
class CustomerForm(forms.ModelForm):
    """
    Since Customer model inherited from User model,
    default fields supply from User model by linking
    CustomerForm to account RegisterForm in views.py
    """

    # no extra fields yet, can add in future
    class Meta:
        model = Customer
        fields = []


""" Note:
Set enctype="multipart/form-data" in form template
to allow file upload 
"""
