from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Liste des annonces</h1> <ul><li>Annonce 1</li><li>Annonce 2</li></ul>')

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1>')
