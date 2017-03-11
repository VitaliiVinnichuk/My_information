from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "command that prints all project models " \
           "and the count of objects in every model"

    def handle(self, **options):
        for ct in ContentType.objects.all():
            try:
                m = ct.model_class()
                output = "%s.%s\t%d" % (m.__module__,
                                        m.__name__,
                                        m.objects.all().count())
                self.stderr.write('Error: {}'.format(output))
                self.stdout.write(output)
            except:
                pass
