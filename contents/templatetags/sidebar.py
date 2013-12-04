from django import template
from django.template import Node
from blogs.models import Category

register = template.Library()


def build_sidebar_menu_list(parser, token):
    """
    {% get_menu_list %}
    """
    return MenuObject()


class MenuObject(Node):
    def render(self, context):
        context['sidebar_menu'] = Category.objects.all()
        return ''


register.tag('get_sidebar_list', build_sidebar_menu_list)