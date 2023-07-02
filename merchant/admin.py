from django.contrib import admin
from .models import Merchant


# Set fields to show in admin dashboard
class MerchantAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "merchant_name",
        "created_at",
        "is_approved",
    )

    # set clickable item to view merchant details
    list_display_links = ("user", "merchant_name")


# Register your models here.
admin.site.register(Merchant, MerchantAdmin)
