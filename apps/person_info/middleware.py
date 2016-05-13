from apps.person_info.models import RequestLogger
from django.conf import settings


class RequestLoggerMiddleware(object):

    def process_request(self, request):
        static_request = request.path.startswith(settings.MEDIA_URL)
        static_request1 = request.path.startswith(settings.STATIC_URL)
        if request.is_ajax() and ('request_logger' in request.path):
            pass
        elif static_request or static_request1:
            pass
        else:
            RequestLogger.objects.create(
                request_method=request.method,
                ip_addr=request.META['REMOTE_ADDR'],
                full_path=request.get_full_path()
            )
        return None
