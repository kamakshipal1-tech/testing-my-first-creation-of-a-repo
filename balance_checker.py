class Account:
    def __init__(self,balance,acc):
        self.balance = balance
        self.acc_no = acc

    def debt(self,amount):
        self.balance -= amount
        print("Debit",amount)
        print("Amount in balance",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Credit",amount)
        print("Amount in balance",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000,4567)
print("Account balance",acc1.get_balance())
print("Account number",acc1.acc_no)
acc1.debt(100)
acc1.credit(100)

