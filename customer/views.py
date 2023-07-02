from django.shortcuts import redirect, render
from .models import User
from .forms import registerForm
from django.contrib import messages


# View to register new customer
def registerCustomer(request):
    """
    New user registration. 'form' from here is
    used in registerUser template. When form is
    valid and saved, it triggers singals and
    print at terminal.
    """
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            # *method 1 - create user from form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # *method 2 - create user from model
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.role = User.CUSTOMER
            user.save()

            # display message, redirect to same register page
            messages.success(request, "Your account is registered")
            return redirect("registerCustomer")

        # if form data is not valid, handle any field errors
        else:
            print(form.errors)

    # if not post method, just display the form
    else:
        form = registerForm()
        print('Error detected in form method')
    
    # pass form to template
    context = {"form": form}

    return render(request, "customer/register.html", context)


"""Note:
To access and use messages object in all templates due to the below in settings.py
'django.contrib.messages.context_processors.messages'

Whatever is returned through context_processors is accessible in all template files
"""
