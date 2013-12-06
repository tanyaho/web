from django.contrib import admin
from rewriteengine.models import htaccess




class htaccessAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['CMS']}),
        (None, {'fields': ['redirection']}),
        (None, {'fields': ['rewrite']}),
        ('Fields available: [Old URL], [Old Query], [New Host], [New URL] if rewrite, [Full New URL] if redirection', {'fields': ['rule']}),
        (None, {'fields': ['condition']}),
        (None, {'fields': ['bulk_upload']}),
    ]


admin.site.register(htaccess, htaccessAdmin)
