from django import forms
from .models import Merchant


# Form for merchant registration
class MerchantForm(forms.ModelForm):
    """
    Since Merchant model inherited from User model,
    other fields will supply from User model by linking
    MerchantForm to account RegisterForm in views.py
    """

    class Meta:
        model = Merchant
        fields = [
            "merchant_name",
            "merchant_license",
        ]


""" Note:
Set enctype="multipart/form-data" in form template
to allow file upload 
"""
