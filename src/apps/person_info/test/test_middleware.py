# -*- coding: utf-8 -*-
import random

from apps.person_info.models import RequestLogger
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

    def test_middleware_logger(self):
        """test add any data to db"""
        RequestLogger.objects.all().delete()
        self.client.get(reverse('request_logger'))
        self.assertEqual(RequestLogger.objects.all().count(), 1)
        last_request = RequestLogger.objects.last()
        self.assertEqual(last_request.full_path, '/request_logger/')
        self.assertEqual(last_request.request_method, 'GET')
        self.assertEqual(last_request.ip_addr, '127.0.0.1')
        # test priority field
        self.assertEqual(last_request.priority, 0)

    def test_template_limit(self):
        """Test for correct response"""
        for i in range(10):
            self.client.get(reverse('index'))
            self.client.get(reverse('request_logger'))
        requests = RequestLogger.objects.all()
        self.assertEqual(requests.count(), 20)
        # elements per page <= 10
        response = self.client.get(reverse('request_logger'))
        requests_count = response.context['requests'].count()
        self.assertEqual(requests_count, 10)

    def test_priority_field(self):
        """Test priority field"""
        for i in range(15):
            self.client.get(reverse('request_logger'))
        for request in RequestLogger.objects.all():
            request.priority = (random.randint(0, 4))
            request.save()
        response = self.client.get(reverse('request_logger'),
                                   {'order_by': '1'})
        requests = response.context['requests']
        priority_list = []
        for i in requests.all():
            priority_list.append(i.priority)
        self.assertEqual(priority_list, sorted(priority_list))
