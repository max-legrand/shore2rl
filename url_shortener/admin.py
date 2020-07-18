from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_url', 'new_url')


admin.site.register(Link, LinkAdmin)
