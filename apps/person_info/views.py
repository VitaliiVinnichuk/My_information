from apps.person_info.models import Person
from django.shortcuts import render


def index(request):
    person = Person.objects.first()
    return render(request, 'person_info/index.html',
                  {'person': person})


def request_logger(request):
    requests = (
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "GET",
            'ip_addr': "192.168.1.1",
            'full_path': "/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "POST",
            'ip_addr': "192.168.1.1",
            'full_path': "/request_logger/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "GET",
            'ip_addr': "2.20.190.43",
            'full_path': "/request_logger/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "GET",
            'ip_addr': "192.168.1.1",
            'full_path': "/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "POST",
            'ip_addr': "192.168.1.1",
            'full_path': "/request_logger/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "GET",
            'ip_addr': "2.20.190.43",
            'full_path': "/request_logger/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "GET",
            'ip_addr': "192.168.1.1",
            'full_path': "/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "POST",
            'ip_addr': "192.168.1.1",
            'full_path': "/request_logger/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "GET",
            'ip_addr': "2.20.190.43",
            'full_path': "/request_logger/"
        },
        {
            'time': "January 26, 2028 13:51:50",
            'request_method': "GET",
            'ip_addr': "192.168.1.1",
            'full_path': "/"
        }
    )
    return render(request, 'person_info/request_logger.html',
                  {'requests': requests})
