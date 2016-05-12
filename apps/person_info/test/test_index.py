# -*- coding: utf-8 -*-
from apps.person_info.models import Person
from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class PersonInfoViewTest(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('index'))

    def test_index(self):
        """test status code"""
        self.assertEqual(self.response.status_code, 200)

    def test_index_html(self):
        """test template render"""
        html = '42 Coffee Cups Test Assignment'
        self.assertTrue(html in self.response.content)
        self.assertContains(self.response, 'Vitalii')


class PersonInfoModelTest(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = Client()

    def test_correct_response(self):
        """test for unicode and object creation"""
        Person.objects.create(first_name=u'Вася',
                              last_name=u'Пупкин',
                              date_of_birth='2000-01-01',
                              bio=u'Вася молодец',
                              email='vasyapupkin@pokemon.com',
                              jabber='vaska007@google.com',
                              skype='Vasya777',
                              other_contacts='9379992')
        new_person = Person.objects.last()
        self.assertEqual(unicode(new_person.first_name), u'Вася')
        # Test corect response after object creation
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Vinnichuk')

    def test_db_data_exist(self):
        """test model data exist objects """
        Person.objects.all().delete()
        response = self.client.get(reverse('index'))
        html_response = 'Error! No person info!'
        self.assertEqual(Person.objects.all().count(), 0)
        self.assertIn(html_response, response.content)
