from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect,render
from . forms import User_register_form
from django.core.exceptions import ValidationError

# Create your views here.






def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
            messages.success(request,"login success Finito")
        else:
            return redirect("account:login")
    return render(request,template_name="login.html",context={})


def logout_user(requset):
    logout(requset)
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = User_register_form(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('home')
    else:
        form = User_register_form()
    return render(request, template_name="register_user.html", context={"form":form})


#






