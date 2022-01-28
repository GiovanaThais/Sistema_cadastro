from django.urls import path

from autenticacao import views
from django.conf import settings
from django.conf.urls.static import static

#fazendo rotas de login e cadastro
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name="sair"), #rota para usuario fazer logout
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
