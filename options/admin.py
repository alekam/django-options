from django.contrib import admin
from .models import *


class OptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'type', 'comment']
    list_filter = ['type', ]
    list_editable = ['value', ]


admin.site.register(Option, OptionAdmin)
