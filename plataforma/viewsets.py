from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication 
from rest_framework import filters

from plataforma import serializers
from rest_framework import generics
#from rest_framework.generics import generics
from .serializers import ImovelSerializer

from plataforma import models

class ImovelViewSet(viewsets.ModelViewSet):
    serializer_class = ImovelSerializer
    queryset = models.Imovel.objects.all()

'''class ListarImoveisAPIView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated, )
    #authentication_classes = [TokenAuthentication

    serializer_class = ImovelSerializer
    queryset = models.Imovel.objects.all()

class ImovelAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Imovel.objects.all()
    serializer_class = ImovelSerializer'''