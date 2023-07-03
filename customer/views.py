from django.shortcuts import redirect, render
from django.contrib import messages
from account.models import Profile, User
from account.forms import RegisterForm
import customer
from .forms import CustomerForm


# View to register new customer
def registerCustomer(request):
    """
    New user registration. 'form' from here is
    used in registerUser template. When form is
    valid and saved, it triggers singals and
    print at terminal.
    """
    # check form data validity
    if request.method == "POST":
        regform = RegisterForm(request.POST)
        byeform = CustomerForm(request.POST)

        # check form data validity
        if regform.is_valid():
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
            user.role = User.CUSTOMER
            user.save()

            # customers show in User model by default, set below to show in Merchant model also
            # get data from byeform, set its user data from customer model to user created above
            customer = byeform.save(commit=False)
            customer.user = user

            # get profile from the user created above, set it to profile in customer model
            profile = Profile.objects.get(user=user)
            customer.profile = profile
            customer.save()

            # display message, redirect to same register page
            messages.success(request, "Your account is registered")
            return redirect("registerCustomer")

        # if form data is not valid, handle any field errors
        else:
            print("Form data posted is not invalid")
            print(regform.errors)

    # if not post method, just display the form
    else:
        regform = RegisterForm()
        byeform = CustomerForm()
        print("Error detected in form method")

    # pass form to template
    context = {
        "regform": regform,
        "byeform": byeform,
    }

    return render(request, "customer/register.html", context)


"""Note:
To access and use messages object in all templates due to the below in settings.py
'django.contrib.messages.context_processors.messages'

Whatever is returned through context_processors is accessible in all template files
"""
