from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h2>Te iubesc mult de tot!</h2>")


def contact_view(*args, **kwargs):
    return HttpResponse("<b>Ce faci mihai?</b>");
