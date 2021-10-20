from accounts.models import Account, GenderChoices
from banks.models import Bank, Branch
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand, CommandError
from random import randint
from transactions.models import Transaction, TransactionTypes

User = get_user_model()


class Command(BaseCommand):
    help = 'create data bank, branch, account, transaction'

    def handle(self, *args, **options):
        user = User.objects.create(username=f"test_user {randint(0, 134243)}", password=make_password("123456"),
                                   type="customer")
        for bank_number in range(10):
            bank_obj = Bank.objects.create(name=f"Test Bank {bank_number}", created_by=user, modified_by=user)
            self.stdout.write(self.style.SUCCESS(f'Bank created successfully {bank_obj}'))
            for branch_number in range(10):
                branch = Branch.objects.create(bank=bank_obj, name=f"Branch {branch_number}",
                                               code=f"test {branch_number}",
                                               address=f"test address {branch_number}",
                                               created_by=user, modified_by=user)
                self.stdout.write(self.style.SUCCESS(f'Branch created successfully {branch}'))
                for account_number in range(10):
                    if account_number < 4:
                        gender_choice = GenderChoices.MALE
                    else:
                        gender_choice = GenderChoices.FEMALE
                    account = Account.objects.create(branch=branch, user=user,
                                                     account_number=int(
                                                         f"{randint(0, 2147483647)}"),
                                                     gender=gender_choice,
                                                     address=f"test account holder address {account_number}",
                                                     balance=100, created_by=user, modified_by=user)
                    self.stdout.write(self.style.SUCCESS(f'Account created successfully {account}'))
                    for transaction_number in range(20):
                        if transaction_number < 9:
                            transaction_type = TransactionTypes.DEBIT
                        else:
                            transaction_type = TransactionTypes.CREDIT

                        transaction = Transaction.objects.create(account=account, amount=transaction_number,
                                                                 type=transaction_type,
                                                                 created_by=user, modified_by=user)
                        self.stdout.write(self.style.SUCCESS(f'Transaction created successfully {transaction}'))
