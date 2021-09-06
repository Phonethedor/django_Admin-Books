from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes', views.clientes, name='clientes'),
    path('sitios', views.sitios, name='clientes'),
    path('leads', views.leads, name='leads'),
    path('docs', views.documentos, name='documentos'),
    path('libros_publicadores', views.libros_publicadores, name='libros_publicadores'),
    path('addB', views.addB, name='addB'),
    path('editB', views.libros_publicadores, name='editB'),
]