from apps.person_info.models import Person
from apps.person_info.templatetags.edit_link import edit_link
from django.core.exceptions import ObjectDoesNotExist
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

    def test_tag_incorect_object(self):
        """Test tag if object not a instance of model"""
        # Object is int
        self.assertRaises(ObjectDoesNotExist, lambda: edit_link(9379992))
        # Object is str
        self.assertRaises(ObjectDoesNotExist, lambda: edit_link('hello'))
        # Blank obj
        self.assertRaises(TypeError, lambda: edit_link())
