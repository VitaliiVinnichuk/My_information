import json
from apps.person_info.forms import PersonForm
from apps.person_info.models import Person, RequestLogger
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    person = Person.objects.first()
    return render(request, 'person_info/index.html',
                  {'person': person})


def request_logger(request):
    requests = RequestLogger.objects.all()[:10]
    if request.is_ajax():
        return HttpResponse(serializers.serialize("json", requests),
                            content_type='application/json')
    return render(request, 'person_info/request_logger.html',
                  {'requests': requests})


@login_required(login_url='/login/')
def edit(request):
    person = Person.objects.all().first()
    if request.method == 'POST' and request.is_ajax():
        form = PersonForm(request.POST,
                          request.FILES,
                          instance=person)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'success': True}),
                                content_type='application/json')
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k]
            return HttpResponse(json.dumps({'success': False,
                                            'errors': response
                                            }))
    form = PersonForm(instance=person)
    return render(request, 'person_info/edit.html', {'form': form})
