from django import forms
from .models import Customer


# Form for merchant registration
class CustomerForm(forms.ModelForm):
    """
    Since Customer model inherited from User model,
    other fields will supply from User model by linking
    CustomerForm to account RegisterForm in views.py
    """

    class Meta:
        model = Customer
        fields = []


""" Note:
Set enctype="multipart/form-data" in form template
to allow file upload 
"""
