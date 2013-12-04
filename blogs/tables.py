import django_tables2 as tables
from django_tables2.utils import A

from blogs.models import Blog


class BlogTable(tables.Table):
    title = tables.LinkColumn('blogs:detail', args=[A('page_slug')])

    class Meta:
        model = Blog
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}