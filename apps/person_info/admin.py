from django.contrib import admin
from apps.person_info.models import Person, RequestLogger

admin.site.register(Person)
admin.site.register(RequestLogger)
