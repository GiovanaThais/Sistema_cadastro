from rest_framework import serializers
from plataforma.models import Cidade, Imovel

#serializando dados do model
class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields ='__all__'
    

class CidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields ='__all__'
