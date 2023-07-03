from django.db import models
from customer.models import User, Profile


# Merchant model
class Merchant(models.Model):
    """
    Model for merchant using existing
    custom User and Profile models
    """

    # fields from User & Profile models
    user = models.OneToOneField(User, related_name="merchant", on_delete=models.CASCADE)
    profile = models.OneToOneField(
        Profile, related_name="merchant", on_delete=models.CASCADE
    )

    # extra fields for MerchantForm
    merchant_name = models.CharField(max_length=50)
    merchant_license = models.ImageField(upload_to="merchants/licence")

    # fields to auto capture
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    # return merchant by merchant_name in admin
    def __str__(self):
        return self.user.email
