from django.shortcuts import render


def index(request):
    person = {
        'first_name': "Vitalii",
        'last_name': "Vinnichuk",
        'date_of_birth': "18-03-1993",
        'bio': "Some bio",
        'email': "vinnichukvitalii@gmail.com",
        'jabber': "vinnich@42cc.co",
        'skype': "vinnichukvitaliy",
        'other_contacts': "mobile tel: +380973755920"
    }
    return render(request, 'person_info/index.html',
                  {'person': person})
