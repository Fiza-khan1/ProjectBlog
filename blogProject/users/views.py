from django.shortcuts import render, redirect
from Blogapp.forms import signupform
from .forms import updateuserprofile,updateuserform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .models import Profile
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign up successful!")
            return redirect('home') 
    else:
        form = signupform()
    
    return render(request, 'users/signup.html', {'form': form})

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request,request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form=AuthenticationForm()
            return render(request,'users/login.html',{'form':form})
    else:
        return redirect('home') 
def userlogout(request):
  
    logout(request)
    return render(request,'users/logout.html')

@login_required
def userprofile(request):
    if request.method=='POST':
        form=updateuserform(request.POST or None,instance=request.user)
        imageform=updateuserprofile(request.POST or None ,request.FILES , instance=request.user.profile)
        if form.is_valid() and imageform.is_valid():
            print("VALID")
            form.save()
            imageform.save()
            redirect('profile')
            
    else:
            form=updateuserform(instance=request.user)
            imageform=updateuserprofile( instance=request.user.profile)
  
    return render(request,'users/profile.html',{'form':form,'imageform':imageform})