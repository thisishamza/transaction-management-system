from django.contrib import admin
from .models import Bank, Branch


class BankAdmin(admin.ModelAdmin):
    list_display = ['name']


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'address']


admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)
