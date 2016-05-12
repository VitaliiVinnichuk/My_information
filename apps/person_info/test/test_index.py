# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class PersonInfoViewTest(TestCase):

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
