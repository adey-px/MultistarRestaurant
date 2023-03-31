from django.shortcuts import render

# Create your views here.
def registerMerchant(request):
    return render(request, "merchant/register.html")
