from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('listing', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 20

admin.site.register(Contact, ContactAdmin)
