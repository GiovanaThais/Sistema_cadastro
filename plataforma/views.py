from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from plataforma.models import Imovel

# Criando views da home
@login_required(login_url='/auth/logar/') #permite que apenas usuarios logados acessem a plataforma
def home(request):
    imoveis = Imovel.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})


