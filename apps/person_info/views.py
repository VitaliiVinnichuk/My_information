from apps.person_info.models import Person
from django.shortcuts import render


def index(request):
    person = Person.objects.first()
    return render(request, 'person_info/index.html',
                  {'person': person})


def request_logger(request):
    return render(request, 'person_info/request_logger.html',
                  {'requests': ''})