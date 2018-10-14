import sys
class Customer:
    ''' Customer bank related operation'''
    bankname="MAYANK_BANK"

    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('After deposit your balance is',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient balance")
            sys.exit()
        self.balance=self.balance-amt
        print("After withdraw your current balance is",self.balance)
    def exit():
        print("Thanks for BANKING")
        sys.exit()
print("Welcome to",Customer.bankname)
name=input("Enter the name")
c=Customer(name)
while True:
    print("d-DEPOSIT\nw-WITHDRAW\ne-exit")
    option=input("Enter the suitable options")
    if option=='d' or option=='D':
        amt=float(input("Enter the amount that you want to deposit"))
        c.deposit(amt)
    elif option=='w' or option=="W":
        amt=float(input("Enter the amount that you want to withdraw"))
        c.withdraw(amt)
    elif option=="e" or option=='E':
        exit()
    else:
        print("Choose the valid options")
