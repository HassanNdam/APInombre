from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Addition
from .serializers import AdditionSerializer

class AdditionView(APIView):
    def post(self, request, *args, **kwargs):
        # Récupérez les données du corps de la requête
        nombre1 = request.data.get('nombre1', 0)
        nombre2 = request.data.get('nombre2', 0)

        # Effectuez l'opération d'addition
        resultat = nombre1 + nombre2

        # Enregistrez les données dans le modèle
        Addition.objects.create(nombre1=nombre1, nombre2=nombre2, resultat=resultat)

        # Sérialisez les données pour la réponse
        serializer = AdditionSerializer(data={'nombre1': nombre1, 'nombre2': nombre2, 'resultat': resultat})
        serializer.is_valid()

        # Retournez la réponse
        return Response(serializer.data, status=status.HTTP_201_CREATED)
