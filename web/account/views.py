from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect,render,get_object_or_404
from . forms import User_register_form,UserForm,UserProfileForm,ChangePasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings


# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        family_name = request.POST.get("family name")
        email = request.POST.get("email")
        print(request.POST)


        #email ourselves the submitted
        subject = "Email from us"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.DEFAULT_FROM_EMAIL]


        # OPTION   1
       # contact_message = "{0},from {1} with email {2}".format(family_name,name,email)


        # Option 2
        context = {
            'user':name,
            'family_name':family_name,
            'email': email
        }

        contact_message = get_template('contact_message.txt').render(context)

        send_mail(subject,contact_message,from_email,to_email,fail_silently=True)
        return redirect("home")


    return render(request,template_name="contact_form.html",context={})




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








def ViewProfile(request):
    context = {}
    template_name = "viewprofile.html"
    return render(request,template_name,context)


def EditProfile (request,username):
    user = User.objects.get(username=username)
    userprofile = UserProfileForm(request.POST or None, instance=request.user)
    user_form = UserForm(request.POST or None, instance=request.user)
    if request.method == "POST":
        if user_form.is_valid() and userprofile.is_valid():
            user_form.save()
            userprofile.save()
            return redirect("home")
    return render(request,template_name = "edit_profile.html",context={"userform":user_form,"userprofile":userprofile})


@login_required
def change_password(request,username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = ChangePasswordForm(user or None, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return render("home")
        else:
            raise ValidationError("no not")
    else:
        form = ChangePasswordForm(user)
    return render(request,template_name="change_password.html",context={"form":form})