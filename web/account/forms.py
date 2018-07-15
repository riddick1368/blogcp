from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError







class User_register_form(forms.Form):
    username = forms.CharField(label="username",max_length=100,min_length=8,widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField( label="Password",
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField( label="conformation password",
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))




    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exist")

        return username

    def clean_email(self):
        email= self.cleaned_data["email"].lower()
        r= User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exist")
        return email


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("password not match")
        return password2



