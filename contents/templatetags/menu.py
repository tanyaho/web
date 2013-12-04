from django import template
from django.template import Node
from contents.models import Content

register = template.Library()


def build_menu_list(parser, token):
    """
    {% get_menu_list %}
    """
    return MenuObject()


class MenuObject(Node):
    def render(self, context):
        context['site_menu'] = Content.objects.all().filter(is_menu=True)
        return ''


register.tag('get_menu_list', build_menu_list)