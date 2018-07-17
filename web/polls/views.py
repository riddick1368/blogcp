from django.shortcuts import render,get_object_or_404 ,redirect
from .models import Poll,Choice
from .forms import Form_poll,Form_choice

# Create your views here.
### poll list
def Poll_list(request):
    poll = Poll.objects.all()
    context = {
        "poll": poll
    }
    template_name= "poll_list.html"
    return render(request,template_name,context)


### poll _detail
def Poll_single(request, id):
    poll = get_object_or_404(Poll, id=id)

    return render(request, template_name="poll_single.html",context={"poll":poll})

### poll create form
def Poll_create(request):
    if request.method =="POST":
        form = Form_poll()
        if form.is_valid():
            form.save()
    return render(request,template_name="poll_create.html",context={})

###poll edite form
def Poll_edit(request,id):
    poll = get_object_or_404(Poll,id=id)
    form =Form_poll(request.POST or None,instance=poll)
    if request.method =="POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request,template_name="poll_edit.html",context={"form":form,"poll":poll})

###poll delete form
def Poll_delete(request,id):
    poll=get_object_or_404(Poll,id=id)
    form = Form_poll(request.POST or None,instance=Poll)
    if request.method=="POST":
        form.delete()
        return redirect("home")
    return render(request,template_name="form_conform_delete.html",context={"form":form,"poll":poll})


def Choice_create(request):
    form = Form_choice()
    if request.method=="POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request,template_name="choice_create.html",name="choice_create")


def choice_delete(request,id):
    choice = get_object_or_404(Choice,id=id)
    form = Form_choice(request.POST or None,instance=choice)
    if request.method =="POST" and form.is_valid():
        form.delete()
        return redirect("home")
    return render(request,template_name="choice_delete.html",name="choice_delete")


def Choice_edit(request,id):
    choice = get_object_or_404(Choice,id=id)
    form = Form_choice(request.POST or None, instance=choice)
    if request.method=="POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request,template_name="choice_edit.html",context={"form":form,"choice":choice})



