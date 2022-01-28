#sistema_cadastro URL Configuration

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from plataforma.viewsets import ListarImoveisAPIView, ImovelAPIView, ListarCidadesAPIView, CidadesAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('', include('plataforma.urls')),

    #rotas da api rest 
    path('api/', ListarImoveisAPIView.as_view(), name='imoveis_api'),
    path('api/<int:pk>/', ImovelAPIView.as_view(), name='imovel_api'),
    path('api/cidades/', ListarCidadesAPIView.as_view(), name='cidades_api'),
    path('api/cidades/<int:pk>/', CidadesAPIView.as_view(), name='cidade_api'),

    #rotas de configuração de token com jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
