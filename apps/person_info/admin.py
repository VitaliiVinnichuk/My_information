from django.contrib import admin
from apps.person_info.models import Person, RequestLogger, ModelActionLog

admin.site.register(Person)
admin.site.register(RequestLogger)
admin.site.register(ModelActionLog)
