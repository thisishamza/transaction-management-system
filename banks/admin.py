from django.contrib import admin
from .models import Bank, Branch


class BankAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Bank, BankAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name','code','address']


admin.site.register(Branch, BranchAdmin)
