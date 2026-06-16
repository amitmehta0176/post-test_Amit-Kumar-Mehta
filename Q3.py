from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def receipt(self):
        pass
class GPay(Payment):
    def pay(self):
        print("payment  done via gpay")

    def receipt(self):
        print("receipt generated successfully")
class CreditCard(Payment):
    def pay(self):
        print("Payment done via Credit Card")

    def receipt(self):
        print("Credit Card receipt generated successfully")   

g1=GPay()
g1.pay()
g1.receipt()

cc1=CreditCard()
cc1.pay()
cc1.receipt()