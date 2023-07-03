from django.contrib import admin
from .models import Customer


# Set fields to show in admin dashboard
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_at",
        "modified_at",
    )

    # # set clickable item to view merchant details
    # list_display_links = ("user", "created_at")


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
