from django.shortcuts import render
from django.http import Http404


# Create your views here.
def commentstore(request):
    raise Http404()

def home(request):
    return render(request, "payapp/home.html")