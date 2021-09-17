from django.contrib import admin

from .models import FinanceExpend, FinanceProfit, FinancePlane


@admin.register(FinanceProfit)
class ProfitAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'timestamp', 'total')


admin.site.register(
    [
        FinancePlane
    ])


@admin.register(FinanceExpend)
class FinanceExpendAdmin(admin.ModelAdmin):
    list_display = ('name', 'total', 'category', 'timestamp')
    search_fields = ('category', 'name',)
