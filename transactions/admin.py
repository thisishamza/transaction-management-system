from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'amount', 'type']
    exclude = ['created_by', 'modified_by']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Transaction, TransactionAdmin)
