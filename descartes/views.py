import csv

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Tecnico, Motivo, Descartes, Guia, Filtro, User
from datetime import datetime  





# Create your views here.


def descartes(request):
    context = {'descartes':Descartes.objects.all(),
                'motivo':Motivo.objects.all(),
                'Tecnico':Tecnico.objects.all(),
                'Guia':Guia.objects.all(),
                'Filtro':Filtro.objects.all(),
                                
    }
    if Descartes.objects.first() is not None:
        linea = Descartes.objects.first().LINEA 
        context["linea"] = linea
    if request.method == "GET":
        if not request.user.is_authenticated:
            user = request.user
            context["user"] = user
            return render(request, "descartes/login.html")
        return render(request, "descartes/descartes.html", context)



def formulario(request):

    user = request.user
    fecha = request.POST.get("fecha")
    producto = request.POST.get("producto")
    lote = request.POST.get("lote")
    motivo = request.POST.get("motivo")
    volumen = request.POST.get("volumen")
    tecnico = request.POST.get("tecnico")
    guia = request.POST.get("guia")
    filtro = request.POST.get("filtro")
    linea = request.POST.get("linea")
    observaciones = request.POST.get("observaciones")
    m = Motivo.objects.get(pk=motivo)
    g = Guia.objects.get(pk=guia)
    f = Filtro.objects.get(pk=filtro)
    t = Tecnico.objects.get(pk=tecnico) 
    descarte = Descartes(fecha=fecha, producto=producto, lote=lote, motivo=m, volumen=volumen, tecnico=t, guia=g, filtro=f, linea=linea, observaciones=observaciones, user=user)
    descarte.save()
    print(m.motivo)
    did = descarte.id 
    print(did)

    data = {"success": True, 
            "user":user.first_name,
            "motivo": m.motivo,
            "guia":g.guia,
            "filtro":f.filtro,
            "tecnico":t.iniciales,
            "fecha":fecha,
            "id":did 
    }

    return JsonResponse(data)


def descaraga(request):
        # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="descartes.csv"'

    writer = csv.writer(response)
    writer.writerow(['fecha', 'producto','lote','motivo',' tecnico','volumen','guia','filtro','linea','user','observaciones'])

    desde= request.POST.get("desde")
    hasta= request.POST.get("hasta")
    print(desde)
    print(hasta)


    for descarte in Descartes.objects.filter(fecha__range=[desde, hasta], borrado=False) :
        writer.writerow([descarte.fecha, descarte.producto, descarte.lote, descarte.motivo, descarte.tecnico, descarte.volumen, descarte.guia, descarte.filtro, descarte.linea, descarte.user, descarte.observaciones])

    return response







def remove(request):
    context = {'descartes':Descartes.objects.all(),
            'motivo':Motivo.objects.all(),
            'Tecnico':Tecnico.objects.all(),
            'Guia':Guia.objects.all(),
            'Filtro':Filtro.objects.all(),
            
                                
    }
    if request.method == "GET":

        return HttpResponseRedirect(reverse("descartes"))
    if request.method == "POST":
        j = request.POST.get('remove')
        print(j)
        
        d = Descartes.objects.get(pk=j)
        print(d.borrado)
        d.borrado = True
        d.save()
        context['mensaje'] = "El descarte ha sido eliminado"
        print(d.borrado)
    return render(request, "descartes/descartes.html", context)






def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("descartes"))
    return render(request, "descartes/login.html", {"message": "Invalid credentials"})



def logout_view(request):
    logout(request)
    return render(request, "descartes/login.html", {"message": "logged out"})