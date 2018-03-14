from account import Account

class CheckingAccount(Account):
    def __init__(self, holder, created_on, account_number, account_type, balance=0.0 ):
        super().__init__(holder, created_on, account_number, account_type, balance)
        
    def charge_interest(self):
        self._balance+=(CheckingAccount.interest*self._balance)
        Account.update_balance(self.balance)
