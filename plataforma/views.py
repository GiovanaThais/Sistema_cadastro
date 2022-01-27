from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from plataforma.models import Imovel


#@login_required(login_url='/auth/logar/') #permite que apenas usuarios logados acessem o portal
def home(request):
    imoveis = Imovel.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})

# Create your views here.
