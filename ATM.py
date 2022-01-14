class ATM(object):
  """
    blueprint for car
  """
#functions#
  def __init__(self, model, color, BankName):
    self.color = color
    self.BankName = BankName
    self.model = model

  def withdraw(self):
    print("Cash has been withdraw")

  def deposit(self):
    print("cash has been deposited")

  def balance(self):
    print("your account balance is 250000")
    


 
ramesh = ATM("bB15", "Black", "ATM")

print(ramesh.withdraw)

