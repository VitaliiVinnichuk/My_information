from apps.person_info.models import Person
from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO


class PrintModelsAndObjectsCount(TestCase):
    fixtures = ['fixtures.json']

    def test_command_output(self):
        """"Test command output"""
        #  prepare output file for command
        out = StringIO()
        # call our command
        call_command('project_models_counter', stdout=out)
        # get command output
        result = out.getvalue()
        # check if we get proper number of objects in database

        self.assertIn('apps.person_info.models.Person	1', result)

        # test command result after create object
        Person.objects.create(first_name='Vasya',
                              last_name='Pupkin',
                              date_of_birth='2000-01-01',
                              bio="Vasya molodec",
                              email='vasyapupkin@pokemon.com',
                              jabber='vaska007@google.com',
                              skype='Vasya777',
                              other_contacts='9379992')
        # call our command
        call_command('project_models_counter', stdout=out)
        # get command output
        result = out.getvalue()
        self.assertIn('apps.person_info.models.Person	2', result)
