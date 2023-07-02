from django import forms
from .models import Merchant


# Form for merchant registration
class merchantForm(forms.ModelForm):
    """
    Since merchant model inherited from User model,
    other fields will supply from User model by linking
    customer registerForm to merchantForm in views.py
    """
    class Meta:
        model = Merchant
        fields = [
            "merchant_name",
            "merchant_license",
        ]

"""Note:
Set enctype="multipart/form-data" in form template
to allow file upload 
"""