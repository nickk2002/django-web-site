from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "index.html", {})


def contact_view(*args, **kwargs):
    return HttpResponse("<b>Ce faci mihai?</b>");
