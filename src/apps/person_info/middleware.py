from apps.person_info.models import RequestLogger
from django.conf import settings


class RequestLoggerMiddleware(object):

    def process_request(self, request):
        media_request = request.path.startswith(settings.MEDIA_URL)
        static_request = request.path.startswith(settings.STATIC_URL)
        if request.is_ajax() and ('request_logger' in request.path):
            return
        if static_request or media_request:
            return
        RequestLogger.objects.create(
                request_method=request.method,
                ip_addr=request.META['REMOTE_ADDR'],
                full_path=request.get_full_path()
            )
