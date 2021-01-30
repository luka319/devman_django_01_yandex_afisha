# views.py
from django.http import HttpResponse
from django.shortcuts import render

def show_one(request):
    print('Кто-то зашёл на главную!')
    return render(request, "one.html")


