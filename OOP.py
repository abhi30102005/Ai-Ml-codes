class BankAccount:
    count=0
    def __init__(self,name, balance):
        self.name=name
        self.__balance=balance
        BankAccount.count+=1

acc1=BankAccount("Abhishek",100_000)
print(acc1.name)
print(acc1._BankAccount__balance)