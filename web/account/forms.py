from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile







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





class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["city","country"]



class UserForm (forms.ModelForm):

    class Meta:
        model = User
        fields = ["username","last_name"]


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(label="old_password",strip=False,widget=forms.PasswordInput(attrs={'autofocus':True}))
    new_password = forms.CharField(label='new_password',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password2 = forms.CharField(label="confirm_password",widget=forms.PasswordInput(attrs={'class':'form-control'}))



    def clean_password(self):
        new1 = self.cleaned_data.get('new_password')
        new2 = self.cleaned_data.get('new_password2')
        if new1 and new2 and new1 != new2:
            raise ValidationError("Password dosen't match")
        return new2


    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise ValidationError("password not valid")
        return old_password