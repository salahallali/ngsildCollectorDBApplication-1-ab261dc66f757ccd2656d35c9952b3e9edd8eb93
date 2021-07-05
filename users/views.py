from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from backend.Email_notifications import Email
from .forms import UserRegisterForm
@login_required
def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')
            alawed_to_update = form.cleaned_data.get('alawed_to_update')
            alawed_to_retrive = form.cleaned_data.get('alawed_to_retrive')
           
            from pymongo import MongoClient
            from backend.Creat_User_For_DB import Create_User_For_Db
            user = Create_User_For_Db(username, password, alawed_to_update)
            messages.success(request, f'Your Account hase been created {username}!^^')
            Email(message=f"new user created!\n{username} \n password: {password}\n email: {email} \n allowed to update: {alawed_to_update}")
            return redirect('Notifications_Reciver-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'users/profile.html')
