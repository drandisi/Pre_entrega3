from django.shortcuts import render
from AppBomberos.models import Bombero
from AppBomberos.forms import *
# Create your views here.

def ver_bomberos(request):

    todos = Bombero.objects.all()

    return render(request, "AppBomberos/verbomberos.html", {"todos":todos})
    
def agregar_bombero(request):

         if request.method == "POST":
 
            miFormulario = Bomberoformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  bombero = Bombero(nombre=informacion["nombre"], 
                  apellido=informacion["apellido"],
                  numero=informacion["numero"],
                  cargo=informacion["cargo"],
                  division=informacion["division"])
                  bombero.save()
                  return render(request, "AppCoder/inicio.html")
         else:
               miFormulario = Bomberoformulario()
 
         return render(request, "AppBomberos/bomberoformulario.html", {"miFormulario": miFormulario})
