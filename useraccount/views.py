from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Profile

#import the rest framework tool
from .serializer import ProfileSerializers, UserSerializer
from rest_framework import status, permissions
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes

#@api_view permet d'accepter seulement le method post
#@permission_classess([permissions.AllowAny]) permet de donne accet a tout le monde
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    #Verifier si la method est post
    if request.method == "POST":
        #Recupere les donners utilisateur avec serializer
        serializer = ProfileSerializers(data=request.data, context={'request', request})
        #si les donner sont valid ont cree un nouveau utilisateur et son profile
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
            #Si l'enregistrement c'est effectuer ont renvoyer les donner 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #si il y'a une erreure ont retour un message d'errure
        return Response(serializer.errors, stauts= status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Method not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def Login(request):
    #Recuperation des données de l'utilisateur
    username = request.data.get("username")
    password = reqeust.data.get('password')

    #Verifier si l'utilisateur est enregistre
    user = authenticate(request, username= username, password=password)
    if user is not None:
        login(requet, user)
        serializer = UserSerializer(user, context={"request", request})
        return Response({'user': serializer.data}, status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


def Logout(request):
    logout(request)
    return redirect('login')

