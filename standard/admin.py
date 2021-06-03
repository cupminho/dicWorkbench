from django.contrib import admin
from .models import Standard
from import_export.admin import ImportExportMixin

class StandardAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Standard, StandardAdmin)