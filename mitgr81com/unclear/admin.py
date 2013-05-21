from django.contrib import admin
from unclear.models import PassphraseHash


class HashAdmin(admin.ModelAdmin):
    readonly_fields = ['access_count', 'slug', ]
    list_display = ('__unicode__', 'access_count', 'max_access')

try:
    admin.site.register(PassphraseHash, HashAdmin)
except: #AlreadyRegistered
    pass
