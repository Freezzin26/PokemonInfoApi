from django.contrib import admin
from .models import Pmdex

# Register your models here.
class PmdexAdmin(admin.ModelAdmin):
    list_display = ('pm_id','pm_name_cn','pm_type')

admin.site.register(Pmdex, PmdexAdmin)