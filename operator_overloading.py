'''
class Bank():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance        
        
    def __sub__(self,other):
        print("substraction:")
        return self.balance-other.balance

    def __lt__(self,pardhu):
        print("lessthan")
        return self.balance<pardhu.balance
    
    def __gt__(self,onr6):
        print("greater than;")
        print(self.balance>onr6.balance)
        
    
ac1=Bank("john",500)
ac2=Bank("ram",900)

print(ac1>ac2)
'''




from abc import ABC,abstractmethod

class Contact_management(ABC):
    @abstactmethod
    def Add_contact(self,name,phone_no):
        pass
    
    @abstractmethod
    def View(self):
        pass
    
    @abstractmethod
    def Change_name(self,old_name,new_name):
        pass