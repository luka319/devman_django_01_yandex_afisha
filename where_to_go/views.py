# views.py
from django.http import HttpResponse

def show_one(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('<h1>Здесь будет карта</h1>')


