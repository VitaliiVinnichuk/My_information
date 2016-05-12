from django.shortcuts import render


def index(request):
    return render(request, 'person_info/index.html')
