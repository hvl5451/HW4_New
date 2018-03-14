from account import Account
class SavingsAccount(Account):
    def __init__(self, holder, created_on, account_number, account_type, balance=0.0):
        super().__init__(holder, created_on, account_number, account_type, balance)
