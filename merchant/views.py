from django.shortcuts import redirect, render
from django.contrib import messages
from account.models import Profile, User
from account.forms import RegisterForm
from .forms import MerchantForm


# View to register new merchant
def registerMerchant(request):
    """
    New merchant registration. 'form' from here is used in
    merchant/register template. When form is valid and saved,
    it triggers singals and print at terminal.
    * get supplied fields, link RegisterForm to MerchantForm
    """
    # check form method, collect data, save user
    if request.method == "POST":
        regform = RegisterForm(request.POST)
        byeform = MerchantForm(request.POST, request.FILES)

        # check form data validity
        if regform.is_valid() and byeform.is_valid():
            first_name = regform.cleaned_data["first_name"]
            last_name = regform.cleaned_data["last_name"]
            username = regform.cleaned_data["username"]
            email = regform.cleaned_data["email"]
            password = regform.cleaned_data["password"]

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.role = User.MERCHANT
            user.save()

            # re-watch
            merchant = byeform.save(commit=False)
            merchant.user = user

            profile = Profile.objects.get(user=user)
            merchant.profile = profile
            merchant.save()

            # display message, redirect to same register page
            messages.success(
                request, "Your account is registered, waiting for approval"
            )
            return redirect("registerMerchant")

        else:
            print("Form data posted is not invalid")
            print(regform.errors)

    # if not post method, just display the form
    else:
        regform = RegisterForm()
        byeform = MerchantForm()
        print("Error detected in form method")

    # pass both forms to template
    context = {
        "regform": regform,
        "byeform": byeform,
    }

    return render(request, "merchant/register.html", context)


""" Note:
Able to access and use messages object in all templates 
due to the below in settings.py
'django.contrib.messages.context_processors.messages'

Whatever is returned through context_processors is 
accessible in all template files
"""
