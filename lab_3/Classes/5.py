class BankAccount:

    print("Write the owner name:")
    owner = input()
    print("Enter your balance")
    balance = int(input())
    print("Write the limit of your balance")
    limit = int(input())

    def deposit(self):
        if self.balance + int(input()) <= self.limit:
            self.balance = self.balance + int(input())
            print(self.balance)
        else:
            print("Sorry, the account overdrawn")

    def withdraw(self):
        if self.balance - int(input()) < 0:
            print("Withdrawals exceed the available balance")
        else:
            self.balance = self.balance - int(input())
            print(self.balance)

acc = BankAccount()
acc.deposit()
acc.withdraw()