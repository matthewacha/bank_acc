class bank_account(self):
"""basic transactions can be performed with this
account"""
  def __init__(self, amount, credit_line=1500):
	self.amount = amount
	self.credit_line = credit_line

  def deposit(self,amount,balance):
    self.balance += self.amount
    return self.balance

  def withdrawal(self,amount, balance):
     if self.amount > self.balance
       return 'Your account balance is low'
     else:
       self.balance-= self.amount
  def check_balance(self, balance):
     return self.balance  
	 
class holder(bank_account):
"""holder class inherits from bank_account"""
  def __init__(self,name,account_number,details={},name_List=[]):
    self.name = name
	self.account_number = account_number
	self.details = details
	self.name_List = name_List
	
  def det(self,name, balance, account_number):
    List.append(self.balance)
	list.append(self.account_number)
	details[self.name]= self.name_List
    
	
	