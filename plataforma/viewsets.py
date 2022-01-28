from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication 
from rest_framework import filters

from plataforma import serializers
from rest_framework import generics
from .serializers import CidadesSerializer, ImovelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from plataforma import models

class ListarImoveisAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    #authentication_classes = [TokenAuthentication

    serializer_class = ImovelSerializer
    queryset = models.Imovel.objects.all()

class ImovelAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Imovel.objects.all()
    serializer_class = ImovelSerializer


class ListarCidadesAPIView(ListCreateAPIView):
    serializer_class = CidadesSerializer
    queryset = models.Cidade.objects.all()

class CidadesAPIView(RetrieveUpdateDestroyAPIView): 
    serializer_class = CidadesSerializer
    queryset = models.Cidade.objects.all()
