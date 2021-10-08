from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['bank', 'user', 'account_no', 'birth_date', 'gender', 'address', 'inital_balance']


admin.site.register(Account, AccountAdmin)
