# -*- coding: utf-8 -*-
from apps.person_info.forms import PersonForm
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class PersonEditTest(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(reverse('edit'))
        self.person = {'first_name': 'Vitaliy',
                       'last_name': 'Vinnichuk',
                       "date_of_birth": "1993-03-18",
                       'bio': 'some bio',
                       'email': 'vinnichukvitaliy@gmail.com',
                       'jabber': 'vinni@42cc.co',
                       'skype': 'vinnichukvitaliy'
                       }

    def test_valid_data(self):
        """test form with valid data"""
        form = PersonForm(self.person)
        self.assertTrue(form.is_valid)

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
