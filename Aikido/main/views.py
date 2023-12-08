from django.shortcuts import render
from django.http import HttpResponse


def proverka(request):
    return render(request,'main/mainstr.html')


def register(request):
    return render(request, 'main/register.html')
