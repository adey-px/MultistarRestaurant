from django.db import models
from account.models import User, Profile


# Customer model
class Customer(models.Model):
    """
    Model for customer using existing 
    custom User and Profile models
    """

    # fields from User & Profile models
    user = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    profile = models.OneToOneField(
        Profile, related_name="customer", on_delete=models.CASCADE
    )

    # fields to auto capture
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # return customer by email in admin
    def __str__(self):
        return self.user.email
