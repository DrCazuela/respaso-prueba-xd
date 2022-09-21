from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    return HttpResponse('<img src="https://steamuserimages-a.akamaihd.net/ugc/418063062072183809/16AA2A62A34EAED74E7163E8B586DF4BE8A43281/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false">')

def vista2(request):
    return HttpResponse('<img src="https://i.imgur.com/LQiOAQj.jpeg">')