# -*- coding: utf-8 -*-
from apps.person_info.models import Person, ModelActionLog
from django.test import TestCase


class PersonEditTest(TestCase):
    fixtures = ['fixtures.json']

    def test_signal_add(self):
        """Test signal"""
        db_changes_before = ModelActionLog.objects.all().count()
        Person.objects.create(first_name=u'Вася',
                              last_name=u'Пупкин',
                              date_of_birth='2000-01-01',
                              bio=u'Вася молодец',
                              email='vasyapupkin@pokemon.com',
                              jabber='vaska007@google.com',
                              skype='Vasya777',
                              other_contacts='9379992')
        db_changes_after = ModelActionLog.objects.all().count()
        self.assertEqual(db_changes_before, db_changes_after - 1)

        # check signal action status

        # After creation
        signal = ModelActionLog.objects.last()
        self.assertEquals(signal.action, 0)

        # After update
        person = Person.objects.get(pk=1)
        person.last_name = 'Test'
        person.save()
        signal = ModelActionLog.objects.last()
        self.assertEquals(signal.action, 1)

        # After delete
        Person.objects.last().delete()
        signal = ModelActionLog.objects.last()
        self.assertEquals(signal.action, 2)
