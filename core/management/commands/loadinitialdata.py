from django.core.management.base import BaseCommand, CommandError
from banks.models import Bank, Branch
from accounts.models import Account, GenderChoices
from transactions.models import Transaction, TransactionTypes
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'create data bank, branch, account, transaction'

    def handle(self, *args, **options):
        try:
            user = User.objects.all()[0]
            for i in range(0, 10):
                bank_obj = Bank(name=f"Test Bank {i}", created_by=user, modified_by=user)
                bank_obj.save()
                self.stdout.write(self.style.SUCCESS(f'Bank created successfully {bank_obj}'))
                for j in range(0, 10):
                    branch = Branch(bank=bank_obj, name=f"Branch {j}", code=f"test {j}", address=f"test address {j}",
                                    created_by=user, modified_by=user)
                    branch.save()
                    self.stdout.write(self.style.SUCCESS(f'Branch created successfully {branch}'))
                    for k in range(0, 10):
                        if k > 4:
                            gender_choice = GenderChoices.MALE
                        else:
                            gender_choice = GenderChoices.FEMALE
                        account = Account(branch=branch, user=user, account_number=int(f"{i}{j}{k}"),
                                          gender=gender_choice, address=f"test account holder address {j}",
                                          balance=100, created_by=user, modified_by=user)
                        account.save()
                        self.stdout.write(self.style.SUCCESS(f'Account created successfully {account}'))
                        for l in range(0, 20):
                            if l < 9:
                                transaction_type = TransactionTypes.DEBIT
                            else:
                                transaction_type = TransactionTypes.CREDIT

                            transaction = Transaction(account=account, amount=l, type=transaction_type,
                                                      created_by=user, modified_by=user)
                            transaction.save()
                            self.stdout.write(self.style.SUCCESS(f'Transaction created successfully {transaction}'))

        except Exception as e:
            self.stdout.write(f'Exception:{e}')
