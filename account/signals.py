from .models import User, Profile
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

""" 
Post_save receiver, to receive signals from sender,
and auto-create user profile. Sender is User model. 
'created' param returns True after user is created. 
Other way to connect to sender:
# post_save.connect(profile_receiver, sender=User)
# import post_save separately 
"""

# Post_save
@receiver(post_save, sender=User)
def create_profile_receiver(sender, instance, created, **kwargs):
    """
    Triggers when user is created, also create their profile.
    When user is updated, also get, update, & save their profile.
    If user with no profle, create their profile, update data.
    """
    if created:
        Profile.objects.create(user=instance)
        print("User profile is created")
    else:
        try:
            profile = Profile.objects.get(user=instance)
            profile.save()
        except:
            Profile.objects.create(user=instance)
            print("No profile found, but it is created")
    print("Success, user is updated")


# Pre_save - optional
@receiver(pre_save, sender=User)
def profile_receiver(sender, instance, **kwargs):
    print("Success, user is saved:", instance.username)
    """
    Triggers before user profile is created, i.e
    after user is created, shortly before profile 
    creation is complete
    """
