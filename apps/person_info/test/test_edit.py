# -*- coding: utf-8 -*-
from apps.person_info.forms import PersonForm
from apps.person_info.models import Person
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class PersonEditTest(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(reverse('edit'))
        self.person = {'first_name': 'Vasya',
                       'last_name': 'Pupkin',
                       "date_of_birth": "2003-03-02",
                       'bio': 'some bio',
                       'other_contacts': '9379992',
                       'email': 'vasya@gmail.com',
                       'jabber': 'vasya@42cc.co',
                       'skype': 'vasya'
                       }

    def test_valid_data(self):
        """test form with valid data"""
        obj = Person.objects.first()
        form = PersonForm(self.person, instance=obj)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(obj.first_name, 'Vasya')
        self.assertEqual(obj.last_name, 'Pupkin')

    def test_blank_data(self):
        """test form for blank field"""
        form = PersonForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'],
                         ['This field is required.'])
        self.assertEqual(form.errors['last_name'],
                         ['This field is required.'])
        self.assertEqual(form.errors['date_of_birth'],
                         ['This field is required.'])

        # test form with not valid data
        obj = Person.objects.first()
        self.assertEqual(obj.first_name, 'Vitalii')
        self.assertEqual(obj.last_name, 'Vinnichuk')

    def test_form_fields(self):
        """check form fields"""
        self.assertIn('name="first_name"', self.response.content)
        self.assertIn('name="last_name"', self.response.content)
        self.assertIn('name="date_of_birth"', self.response.content)
        self.assertIn('name="email"', self.response.content)
        self.assertIn('name="jabber"', self.response.content)

    def test_render_widget(self):
        """Check correct work custom widget
        which add 'datepicker' class into DateTime widget"""
        self.assertIn('datepicker', self.response.content)
