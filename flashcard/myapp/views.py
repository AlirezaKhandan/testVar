from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#def coreDef(request):

    #return render(request, 'index.html')



@api_view(['GET'])
def version(request):
    return Response({"version": "1.0.0"})