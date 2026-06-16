## QUESTION NUMBER 01
class BankAccount:
    def __init__(self):
        self.__balance=10000

    def deposit(self,amount):
        self.__balance+=amount
        print("Bankbalance after deposit",self.__balance) 

    def withdrawal(self,amount):
        if(amount>self.__balance):
            print("print insuffcient  ")
        else:
            self.__balance-=amount 
            print("amount after withdrawal :",self.__balance)  

    def get_balance(self):
        print("current balance :",self.__balance)        
account1=BankAccount()    
account1.deposit(2500)
account1.withdrawal(1500)
account1.get_balance()  

print()
account2=BankAccount()  
account2.deposit(12000)
account2.withdrawal(800)
account2.get_balance()         
