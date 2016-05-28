from apps.person_info.models import Person
from django.core.urlresolvers import reverse
from django.template import Template
from django.template.context import Context
from django.test import TestCase


class TemplateTagTest(TestCase):
    fixtures = ['fixtures.json']

    def test_tag(self):
        """Test custom tag"""
        self.client.login(username="admin", password="admin")
        person = Person.objects.first()
        template = Template("{% load edit_link %}"
                            "{% edit_link person %}")
        render_result = template.render(Context({'person': person}))
        self.assertIn(reverse('admin:person_info_person_change',
                              args=(person.id,)), render_result)
