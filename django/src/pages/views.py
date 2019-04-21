from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kargs):
    print(args, kargs)
    print(request.user)
    return render(request, "base.html", {})