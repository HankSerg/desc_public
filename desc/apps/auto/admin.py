from django.contrib import admin

from .models import Auto, Action

admin.site.register(Auto)


@admin.register(Action)
class AutoItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'auto', 'created_date', 'updated_date')
