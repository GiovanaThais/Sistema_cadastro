from django.contrib import admin
from .models import Imovel, Cidade, Imagem


@admin.register(Imovel)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'valor', 'quartos', 'tamanho', 'rua', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')
    
admin.site.register(Imagem)
admin.site.register(Cidade)
# Register your models here.
