from django.contrib import admin
from .models import Bank, Branch


class BankAdmin(admin.ModelAdmin):
    list_display = ['name']
    exclude = ['created_by', 'modified_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['bank', 'name', 'code', 'address']
    exclude = ['created_by', 'modified_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)
