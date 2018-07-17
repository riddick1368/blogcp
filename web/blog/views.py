from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post
from .forms import Form_post
from django.core.exceptions import ValidationError


from django.contrib.auth.decorators import login_required

# Create your views here.

def Post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    context={"post":post}
    template= "post_single.html"
    return render(request,template,context)




def Post_list(request):
    post = Post.objects.all()

    context={
        "post":post
    }

    template_name = "post_list.html"


    return render(request,template_name,context)







def Post_create(request):
    form = Form_post()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request,template_name="post_create.html",context={"form":form})

def post_delete(request,id):
    post  = get_object_or_404(Post,id=id)
    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request,template_name="post_delete.html",context={})



def post_edit(request,id):
    post = get_object_or_404(Post,id=id)
    form = Form_post(request.POST or None,instance=post)
    if request.method =="POST" and form.is_valid():
        form.save()
        return redirect("home")


    return render(request,template_name="post_edit.html",context={'form':form,"post":post})













