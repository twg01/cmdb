from django.shortcuts import render,redirect,render_to_response

from .models import User
# Create your views here.

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        userobj = User.objects.all().values()

        return redirect("/")
    else:
        return render_to_response("login.html")