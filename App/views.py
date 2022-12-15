from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.db import IntegrityError


# Create your views here.
def index(request):
    return render(request, 'App/index.html')


def singup(request):
    if request.method == 'GET':
        return render(request, 'App/singup.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            
            try:
                user = User.objects.create_user(
                    request.POST["username"],
                    password=request.POST["password1"])
                user.save()
                login(request, user)
                print('ok')
                return redirect('tasks')
          
            except IntegrityError:
                return render(request, 'App/singup.html', {
                    'form' : UserCreationForm,
                    'error' : 'Username alredy exists'
                })
               
        return render(request, 'App/singup.html', {
            'form' : UserCreationForm,
            'error' : 'password no match'
                }) 

  
def tasks(request):
    return render(request, 'App/tasks.html')                    

    