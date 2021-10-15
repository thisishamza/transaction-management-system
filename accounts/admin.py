from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['branch', 'user', 'account_number', 'birth_date', 'gender', 'address', 'balance']
    exclude = ['created_by', 'modified_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Account, AccountAdmin)
