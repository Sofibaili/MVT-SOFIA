from django.shortcuts import render
from AppFamilia.models import Familiar

def index(request):
    return render(request, "AppFamilia/saludar.html")

# Create your views here.

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "AppFamilia/familiares.html",
                {"lista_familiares": lista_familiares})