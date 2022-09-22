from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gatopan(request):
    return HttpResponse('<img src="https://scontent.fccp2-1.fna.fbcdn.net/v/t1.18169-9/180562_192037007483244_7485296_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=bNY2AGnCLIEAX-lnuq3&_nc_ht=scontent.fccp2-1.fna&oh=00_AT996aDTAkpWvH0OHN4toz50IrqH4WCYuLPEHhoepV28eg&oe=63517815">')

def gatopan2(request):
    return HttpResponse('<img src="https://scontent.fccp2-1.fna.fbcdn.net/v/t1.18169-9/311283_263529020334042_1020146402_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=174925&_nc_ohc=SSbb0CAL8RkAX_2BZ-P&_nc_ht=scontent.fccp2-1.fna&oh=00_AT-xGd_JEt-svY95wHet6z9WlxavMRkYLAWBLgO4tgpevw&oe=63516F50">')