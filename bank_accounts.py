class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        # used .2f for a float of two decimal places

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit Complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account {self.name} only has a balance of ${self.balance:.2f}")
        
    def withdrawal(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdrawal Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}.")

    def transfer(self, amount, account):
        try:
            print("**********\n\nBeginning Transfer... 🚀")
            self.viableTransaction(amount)
            self.withdrawal(amount)
            account.deposit(amount)
            print("\nTransfer Complete. ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interruped ❌ {error}")

class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdrawal(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdrawal complete")
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: ❌ {error}")
                
