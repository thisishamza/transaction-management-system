from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'amount', 'type', 'timestamp']


admin.site.register(Transaction,TransactionAdmin)
