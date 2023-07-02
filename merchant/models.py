from django.db import models
from customer.models import User, Profile


# Merchant model
class Merchant(models.Model):
    """
    Model for merchant using existing custom
    User and UserProfile models.
    """

    # fields supplied from User model
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    profile = models.OneToOneField(
        Profile, related_name="profile", on_delete=models.CASCADE
    )

    # extra fields for merchantForm
    merchant_name = models.CharField(max_length=50)
    merchant_license = models.ImageField(upload_to="merchants/licence")

    # fields to auto capture
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # identify merchant by name
    def __str__(self):
        return self.merchant_name
