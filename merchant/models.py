from django.db import models
from customer.models import User, UserProfile

# Merchant model
class Merchant(models.Model):
    """
    Model for merchant using existing custom
    User and UserProfile models.
    """

    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    user_profile = models.OneToOneField(
        UserProfile, related_name="userprofile", on_delete=models.CASCADE
    )
    merchant_name = models.CharField(max_length=50)
    merchant_license = models.ImageField(upload_to="merchants/licence")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.merchant_name
