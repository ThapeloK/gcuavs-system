from django.contrib import admin

from .models import AV_Request


admin.site.site_header = "Ticket System Administration"
admin.site.site_title = "GCUAVS Ticket System Admin Area"
admin.site.index_title = "Welcome GCUAVS Ticket System"


class AV_RequestAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['title']}),
    ('Data Information', {'fields':['date_posted'], 'classes': ['collapse']}),]

admin.site.register(AV_Request)