from django.shortcuts import render
from django.http import HttpResponse
from .models import Register

def register(request):
    return render(request,"register.html")

def register_action(request):
    id = request.GET.get("id")
    return HttpResponse(id)

# Create your views here.
