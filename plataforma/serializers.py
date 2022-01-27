from rest_framework import serializers
from .models import Imovel, Cidade, Imagem


class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields ='__all__'
    
class CidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields ='__all__'

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields ='__all__'