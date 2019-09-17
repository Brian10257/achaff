from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('city', 'title', )
    list_filter = ('realtor', 'city' )
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
    list_per_page = 20
admin.site.register(Listing, ListingAdmin)