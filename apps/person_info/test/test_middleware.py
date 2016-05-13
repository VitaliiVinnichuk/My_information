# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class MiddleWareLoggerViewTest(TestCase):
    """Middleware test"""

    def setUp(self):
        self.client = Client()

    def test_request_logger(self):
        """test status code"""
        response = self.client.get(reverse('request_logger'))
        self.assertEqual(response.status_code, 200)

    def test_request_logger_html(self):
        """test template render"""
        html = '42 Coffee Cups Test Assignment'
        response = self.client.get(reverse('request_logger'))
        self.assertTrue(html in response.content)
        template_name = 'person_info/request_logger.html'
        self.assertTemplateUsed(response, template_name)
        self.assertContains(response, '/request_logger/')
        self.assertContains(response, 'GET')
        self.assertContains(response, '2.20.190.43')
