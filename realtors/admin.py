from django.contrib import admin

from .models import Realtor
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'hire_date' )
    list_display_links = ('email', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Realtor, RealtorAdmin)
 