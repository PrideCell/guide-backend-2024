from django.contrib import admin

from .models import Log  
class LogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'team_id', 'action')
    ordering = ('timestamp',)
    search_fields = ('team_id', 'action')

admin.site.register(Log, LogAdmin)


#should try exports