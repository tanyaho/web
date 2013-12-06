from django.contrib import admin
from blogs.models import Blog, Comment, Category, FileUpload


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3
    fieldsets = [

        ('Advanced', {'fields': ('user', 'comment'), 'classes': ['collapse']}),

    ]

class FileInline(admin.StackedInline):
    model = FileUpload
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['pub_date']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['category']}),
        (None, {'fields': ['page_slug']}),
        ('Advanced', {'fields': ['is_comment']}),
    ]
    inlines = [CommentInline,FileInline]
    prepopulated_fields = {"page_slug": ("title",)}



admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['page_slug']}),
    ]
    prepopulated_fields = {"page_slug": ("title",)}



admin.site.register(Category, CategoryAdmin)