from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
#import the rest framework tool
from .serializer import ProfileSerializers
from rest_framework import status, permissions
from rest_framework.response import response 

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         lastName = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password = request.POST.get('password')
#         langageToLearning = request.POST.get('langage')
#         profile_image = request.FILES.get('profile',Profile.profile_image.default)
#         if password1 == password:
        
#             if username and email and langageToLearning:
#                 if User.objects.filter(email=email).exists():
#                     messages.info(request, 'Email already exists')
#                     return redirect("register") 
#                 else:
#                     new_user = User.objects.create_user(username =username, email = email, password= password)
#                     new_user.last_name = lastName
#                     new_user.save()

#                     if Profile.objects.filter(user=new_user).exists():
#                         messages.info(request, "this personne is already registreted")
#                         return redirect('register')
#                     else:
#                         profile = Profile.objects.create(user=new_user, langage=langageToLearning, profile=profile_image)
#                         profile.save()
#                         return redirect('index')
#             else:
#                 messages.info(request, 'Les informations ne sont pas complete')
#                 return redirect("register")
#         else:
#             messages.info(request, "Password is not matching ")
#             return redirect("register")

#     return HttpResponse('<h1>register page </h1>')

def register(request):
    if request.method == "POST":
        serializer = ProfileSerializers(data=request.data, context={'request', request})
        if serializer.is_valid():
            user_data = serializer.validated_data['user']
            user = User.objects.create_user(
                username = user_data['username'],
                email = user_data['email'],
                password = user_data['password'],
                last_name = user_data['last_name']
                
            )
            profile = Profile.objects.create(
                user=user,
                langage= serializer.validated_data['langage'],
                profile_image = serializer.validated_data.get('profile', Profile.profile_image.default)
            )


            return response(serializer.data, status=status.HTTP_201_CREATED)
        return response(serializer.errors, stauts= status.HTTP_400_BAD_REQUEST)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login = login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'username or password is not identifier')
            return redirect('login')
    
    return HttpResponse('<h1>login page</h1>')

def Logout(request):
    logout(request)
    return redirect('login')

