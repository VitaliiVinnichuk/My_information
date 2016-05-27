from apps.person_info.models import Person
from django.core.urlresolvers import reverse
from django.template import Template
from django.test import TestCase


class TemplateTagTest(TestCase):
    fixtures = ['fixtures.json']

    def test_tag(self):
        """Test custom tag"""
        self.client.login(username="admin", password="admin")
        person = Person.objects.first()
        template = Template("{% load person_info tags %}",
                            "{% edit_link person %}").render(context={'person':person})
        print reverse('admin:person_info_person_change')
        self.assertIn(reverse('admin:person_info_person_change'), template)
