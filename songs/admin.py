from django.contrib import admin
from .models import Song, IP
# @admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_per_page = 2
    model = Song
    # list_per_page = 1 # No of records per page



admin.site.register(Song, SongAdmin)
admin.site.register(IP)