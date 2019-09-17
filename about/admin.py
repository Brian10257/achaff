from django.contrib import admin

from .models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'sub_title2')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title', 'sub_title')
    search_fields = ('title', 'sub_title')
    list_per_page = 20
admin.site.register(About, AboutAdmin)