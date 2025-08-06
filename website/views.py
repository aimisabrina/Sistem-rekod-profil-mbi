from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . models import User

# Start views below
def index(request):
    if request.method == 'POST':
        userid = request.POST.get('id')
        password = request.POST.get('password')

        try:
            user = User.objects.get(userid=userid, password=password)
            request.session['id'] = user.userid  # simpan dalam session
            return render(request,'dashboard.html', {'message': 'Sucessfully Login'})
        except User.DoesNotExist:
            return render(request, 'index.html', {'message': 'Invalid User ID or Password',})
    return render (request,"index.html")

def dashboard(request):
    return render (request, "dashboard.html")

def senaraisistem(request):
    return render (request, "senaraisistem.html")

def sistembaharu(request):
    return render (request, "sistembaharu.html")
