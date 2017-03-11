from django import template
from django.core.urlresolvers import reverse
from django.template import TemplateSyntaxError

register = template.Library()


@register.simple_tag()
def edit_link(object):
    """Custom tag which get a object and render link to it
    admin page"""
    try:
        app = object._meta.app_label
        module = object._meta.module_name
        url = reverse('admin:%s_%s_change' % (app, module),  args=[object.id])
        return u'<a href="%s">Admin %s</a>' % (url,  object.__unicode__())
    except Exception as e:
        raise TemplateSyntaxError(e)
