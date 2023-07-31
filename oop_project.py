from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdrawal(10000)
Dave.withdrawal(20)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)


Jim = InterestRewardsAccount(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAccount(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(1000, Sara)
