class Account:


    def __init__(self,filepath):
     self.filepath=filepath
     with open(filepath,'r')as file:
        self.balance=int(file.read())


    def withdraw(self,ammount):
        self.balance=self.balance-ammount

    
    def deposit(self,ammount):
        self.balance=self.balance+ammount


    def commit(self):
        with open(self.filepath,'w')as file:
            file.write(str(self.balance))

            
account=Account("account//balance.txt")
print(account.balance)
account.withdraw(300)
print(account.balance)
account.commit()