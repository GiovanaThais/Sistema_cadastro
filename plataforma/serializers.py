from rest_framework import serializers
from plataforma.models import Cidade, Imovel


class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields ='__all__'
    

class CidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields ='__all__'
