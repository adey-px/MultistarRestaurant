from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Manager for creating user & superuser
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("Email address is required")

        if not username:
            raise ValueError("Please provide a username")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    # create superuser from user above
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.superadmin = True

        user.save(using=self._db)
        return user


# Custom User model
class User(AbstractBaseUser):
    CUSTOMER = 1
    MERCHANT = 2

    # set roles for user choice
    roles = {
        (CUSTOMER, "Customer"),
        (MERCHANT, "Merchant"),
    }

    # set table fields for user account in db
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, blank=True)
    role = models.PositiveIntegerField(choices=roles, blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    # pass UserManager above, override built in User model
    # set this model update to tell django in settings.py
    objects = UserManager()

    # return user by email
    def __str__(self):
        return self.email

    # set admin & superadmin access permit
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


""" Note:
Custom Profile model is linked to custom User model above.
- user here is same user instance above.
- set django signal to auto create profile as user is created.
"""


# Custom Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="users/profile_images", blank=True, null=True
    )
    cover_image = models.ImageField(
        upload_to="users/cover_images", blank=True, null=True
    )

    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)

    pin_code = models.CharField(max_length=150, blank=True, null=True)
    latitude = models.CharField(max_length=150, blank=True, null=True)
    longitude = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    # return profile by email
    def __str__(self):
        return self.user.email
