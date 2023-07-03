from django.contrib import admin
from .models import Merchant


# Set fields to show in admin dashboard
class MerchantAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "merchant_name",
        "created_at",
        "modified_at",
        "is_approved",
    )

    # # set clickable item to view merchant details
    # list_display_links = ("merchant_name", "user")


# Register your models here.
admin.site.register(Merchant, MerchantAdmin)
