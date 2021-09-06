from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    clientes = Client.objects.all()
    context = {
        'lista_clientes': clientes,
    }

    return render(request, 'polls/home.html', context)


def clientes(request):
    clientes = Client.objects.all()
    context = {
        'lista_clientes': clientes,
    }

    return render(request, 'polls/cliente.html', context)


def sitios(request):
    sitios = Site.objects.all()
    context = {
        'lista_sitios': sitios,
    }

    return render(request, 'polls/sitios.html', context)


def leads(request):
    leads = Lead.objects.all()
    context = {
        'lista_leads': leads,
    }

    return render(request, 'polls/leads.html', context)


def documentos(request):
    documentos = Documento.objects.all()
    context = {
        'lista_documentos': documentos,
    }

    return render(request, 'polls/docs.html', context)


def libros_publicadores(request):
    libros = Libro.objects.all()
    publicadores = Publicador.objects.all()

    context = {
        'lista_libros': libros,
        'lista_publicadores': publicadores,
    }

    return render(request, 'polls/libros.html', context)

def addB(request):
    if request.POST['titulo']:
        Libro.objects.create(titulo=request.POST['titulo'])
    return redirect("libros_publicadores")