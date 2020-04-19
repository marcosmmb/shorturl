from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ("slug", "counter")


admin.site.register(Link, LinkAdmin)
