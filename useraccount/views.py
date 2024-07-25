from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password = request.POST.get('password')
        langageToLearning = request.POST.get('langage')
        
        print(password1)
        if password1 == password:
        
            if username and email and langageToLearning:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists')
                    return redirect("register")
                else:
                    new_user = User.objects.create_user(username=username, email=email, password=password )
                    new_user.save()
                    return redirect('index')
            else:
                messages.info(request, 'Les informations ne sont pas complete')
                return redirect("register")
        else:
            messages.info(request, "Password is not matching ")
            return redirect("register")

    return HttpResponse('<h1>register page </h1>')
