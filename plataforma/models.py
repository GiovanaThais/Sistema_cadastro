from django.db import models
from django.contrib.auth.models import User

class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url

class Cidade(models.Model):
    nome = models.CharField("nome", max_length=30)

    def __str__(self) -> str:
        return self.nome

class Imovel(models.Model):
    choices = (('V', 'Venda'),
                ('A', 'Aluguel'))

    choices_imovel = (('A', 'Apartamento'),
                        ('C', 'Casa'))

    imagens = models.ManyToManyField(Imagem)
    valor = models.FloatField()
    quartos = models.IntegerField()
    tamanho = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    rua = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=choices)
    tipo_imovel = models.CharField(max_length=1, choices=choices_imovel)
    numero = models.IntegerField()
    bairro = models.TextField()
    contato = models.CharField("telefone", max_length = 100)


    def __str__(self) -> str:
        return self.rua
    
    class Meta:
        verbose_name = "Imóvel" 
        verbose_name_plural = "Imóveis"
# Create your models here.
