from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(requests):
    if requests.method == 'POST':
        username = requests.POST.get("username")
        email = requests.POST.get('email')
        password1 = requests.POST.get('password1')
        password = requests.POST.get('password')
        langageToLearning = requests.POST.get('langage')

        if password1 == password:
        
            if username and email and langageToLearning:
            
                if User.objects.get(email=email).exitst():
                    return messages.info(request, 'Email already exists')
                else:
                    new_user = User.objects.create_user(username=username, email=email, )
            else:
                return messages.info(requests, 'Les informations ne sont pas complete')
        else:
            return messages.info(requests, "Password is not matching ")

    return HttpResponse('<h1>register page </h1>')
