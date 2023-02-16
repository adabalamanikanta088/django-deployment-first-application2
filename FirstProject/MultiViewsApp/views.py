from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f1(request):
    return HttpResponse("<h2>GOOD mrng MY DEAR FRIENDS...!.</h2><hr/>");
    
def f2(request):
    return HttpResponse("<h2>GOOD aftr MY DEAR FRIENDS...!.</h2><hr/>");
    
def f3(request):
    return HttpResponse("<h2>GOOD evng MY DEAR FRIENDS...!.</h2><hr/>");
