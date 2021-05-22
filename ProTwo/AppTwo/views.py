from django.shortcuts import render
#from django.http import HttpResponse
from AppTwo.models import User
from . import forms
from AppTwo.forms import NewUserForm
# Create your views here.

def index(request):
    my_dictionary={'insert_me':"Hello i'm from views.py"}
    return render(request,'AppTwo/index.html',context=my_dictionary)

def help(request):
    help_dictionary={'help_me':"Please leave a message for our help"}
    return render(request,'AppTwo/help.html',context=help_dictionary)

def user(request):
    name_list = User.objects.order_by('first_name')
    name = {'list': name_list}
    return render(request,"AppTwo/user.html",context=name)


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error")

    return render(request,"AppTwo/users.html",{"form":form})
