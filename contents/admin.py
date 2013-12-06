from django.contrib import admin
from contents.models import Content, Images, slideshow


class ImagesInline(admin.StackedInline):
    model = Images
    extra = 1


class SlideshowsInline(admin.StackedInline):
    model = slideshow
    extra = 1


class ContentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['pub_date']}),
        (None, {'fields': ['description']}),
        ('SEO', {'fields': ('page_slug', 'meta_title', 'meta_description')}),
        ('Advanced', {'fields': ['is_menu']}),
    ]
    inlines = [ImagesInline, SlideshowsInline]
    prepopulated_fields = {"page_slug": ("title",)}


admin.site.register(Content, ContentAdmin)
