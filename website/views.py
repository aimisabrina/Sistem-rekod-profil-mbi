from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request,"index.html")

def dashboard(request):
    return render (request, "dashboard.html")

def senaraisistem(request):
    return render (request, "senaraisistem.html")

def sistembaharu(request):
    return render (request, "sistembaharu.html")
