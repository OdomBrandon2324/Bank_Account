class BankAccount:
    
    def __init__(self, int_rate, balance= 0): 
        self.balance = balance
        self.int_rate = int_rate / 100


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance-= 5
            print(" Insufficent funds")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self 

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

firstAccount = BankAccount{10,0}
firstAccount =  deposit{100}.withdraw{0}.display_account_info{}.yield_interest{}




class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account
        self.account = BankAccount(int_rate=2, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return

    def account_balance(self):
        print(f"User {self.name} has a balance of {self.account.balance}")


my_user = User("Brandon", "broyjones@hotmail")
my_user.make_depsosit(100).make_withdrawal(20).account_balance()













