from django.shortcuts import render


def index(request):
    name = 'Kiel'
    return render(request, 'index.html', {'name':name})