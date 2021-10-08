from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['bank', 'user', 'account_number', 'birth_date', 'gender', 'address', 'balance']


admin.site.register(Account, AccountAdmin)
