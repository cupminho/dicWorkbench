from django.contrib import admin
from .models import History
from import_export.admin import ImportExportMixin

class HistoryAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(History, HistoryAdmin)