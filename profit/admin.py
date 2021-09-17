from django.contrib import admin

# Register your models here.
from .models import Profit

# @admin.register(Profit)
# class ProfitAdmin(admin.ModelAdmin):
#     list_display = ('name','category','timestamp','total')
    # fields = ['name', 'timestamp']


# admin.site.register(Profit, ProfitAdmin)