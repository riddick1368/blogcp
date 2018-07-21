from django.shortcuts import render,get_object_or_404 ,redirect
from .models import Poll,Choice
from .forms import Form_poll,Form_choice
from django.contrib import messages

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
    form = Form_poll(request.POST)
    if request.method =="POST":
        if form.is_valid():
            form.save()
    return render(request,template_name="poll_create.html",context={"form":form})

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
    poll = get_object_or_404(Poll,id=id)
    if request.method =="POST":
        poll.delete()
        return redirect("home")
    return render(request,template_name="confrom_delete.html",context={"poll":poll,})


def Choice_create(request,id):
    poll = get_object_or_404(Poll,id=id)
    form = Form_choice(request.POST)
    if request.method=="POST" and form.is_valid():
        new_choice = form.save(commit=False)
        new_choice.poll = poll
        new_choice.save()
        return redirect("home")
    return render(request,template_name="choice_create.html",context={"form":form})


def choice_delete(request,id):
    choice = get_object_or_404(Choice,id=id)
    if request.method =="POST":
        choice.delete()
        return redirect("home")
    return render(request,template_name="choice_delete.html",context={"choice":choice})


def Choice_edit(request,id):
    choice = get_object_or_404(Choice,id=id)
    poll = get_object_or_404(Poll,id=choice.poll.id)
    form = Form_choice(request.POST or None, instance=choice)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,template_name="choice_edit.html",context={"poll":poll,"form":form,"choice":choice , "edit_mode":True})



