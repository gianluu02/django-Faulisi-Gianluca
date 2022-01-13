from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("Homepage!")

def chi_siamo(request):
    return HttpResponse("<h2>Pagina: Chi siamo</h2>")

def contatti(request):
     return HttpResponse("Contattaci!")