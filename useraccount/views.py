from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Profile

#import the rest framework tool
from .serializer import ProfileSerializers, UserSerializer
from rest_framework import status, permissions
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
#import the rest_framewok_simplejwt moduls
from rest_framework_simplejwt.tokens import RefreshToken

#@api_view permet d'accepter seulement le method post
#@permission_classess([permissions.AllowAny]) permet de donne accet a tout le monde
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    

    #Verifier si la method est post
    if request.method == "POST":
        #Recupere les donners utilisateur avec serializer
        
        serializer = ProfileSerializers(data=request.data, context={'request': request})
        
        #si les donner sont valid ont cree un nouveau utilisateur et son profile
        if serializer.is_valid():
            
            serializer.save()

            #Si l'enregistrement c'est effectuer ont renvoyer les donner 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #si il y'a une erreure ont retour un message d'errure
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Method not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def Login(request):
    #Recuperation des données de l'utilisateur
    username = request.data.get("username")
    password = request.data.get('password')

    #Verifier si l'utilisateur est enregistre
    user = authenticate(request, username= username, password=password)
    if user is not None:
        #pour genere le token de l'utilisateur
        refresh = RefreshToken.for_user(user)

        login(request, user)
        serializer = UserSerializer(user, context={"request": request})
        
        return Response({'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serializer.data}, status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def Logout(request):
    logout(request)
    return Response({'details': "logged succesfull"}, status=status.HTTP_200_OK)

