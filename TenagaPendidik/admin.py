from django.contrib import admin
from TenagaPendidik.models import TenagaPendidik
# Register your models here.

class TenagaPendidikAdmin(admin.ModelAdmin):
    list_display = ['no', 'nip','nama', 'jabatan']
    search_fields = ['nip','nama']
    

admin.site.register(TenagaPendidik, TenagaPendidikAdmin)