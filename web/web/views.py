from django.shortcuts import render






def home(requset):
    context = {}
    template_name= "home.html"
    return render(requset,template_name,context)