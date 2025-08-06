from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Start views below
def login_view(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")

        # authenticate uses username by default
        user = authenticate(request, username=user_id, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")   
        else:
            messages.error(request, "Invalid ID or Password")

    return render(request, "index.html") 

def dashboard(request):
    return render (request, "dashboard.html")

def senaraisistem(request):
    return render (request, "senaraisistem.html")

def sistembaharu(request):
    return render (request, "sistembaharu.html")
