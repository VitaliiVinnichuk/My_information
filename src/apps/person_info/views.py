import json
from apps.person_info.forms import PersonForm
from apps.person_info.models import Person, RequestLogger
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import signal_processor  # noqa


def index(request):
    person = Person.objects.first()
    return render(request, 'person_info/index.html',
                  {'person': person})


def request_logger(request):
    # order request list
    order_by = request.GET.get('order_by', '')
    requests = RequestLogger.objects.all()
    if order_by:
        if order_by == '0':
            requests = requests.order_by('-priority')[:10]
        if order_by == '1':
            requests = requests.order_by('priority')[:10]
    else:
        requests = requests.order_by('-time')[:10]
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
