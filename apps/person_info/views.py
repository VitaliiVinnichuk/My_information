from apps.person_info.models import Person, RequestLogger
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    person = Person.objects.first()
    return render(request, 'person_info/index.html',
                  {'person': person})


def request_logger(request):
    requests = (RequestLogger.objects.all().order_by('-time'))[:10]
    if request.is_ajax():
        return HttpResponse(serializers.serialize("json", requests),
                            content_type='application/json')
    return render(request, 'person_info/request_logger.html',
                  {'requests': requests})


def edit(request):
    persons = Person.objects.all().first()
    return render(request, 'person_info/edit.html', {'form': persons})
