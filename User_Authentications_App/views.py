
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from User_Authentications_App.forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home_view(request):
    context = {
        "user" : request.user
    }
    return render(request,'home.html',context)

def register_view(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f"{username} account create successfully.")
            return redirect('login')
        else:
            username = form.cleaned_data.get('username')
            messages.warning(request,f"{username} account not created.")
            return redirect('register')
    else:
       form = UserRegisterForm()
       return render(request,'register.html',{'form':form})