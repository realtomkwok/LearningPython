class Account:
    def __init__(self, name, balance):
        self.owner = name,
        self.balance = balance
    
    def __repr__(self):
        return """
        {}'s account:
        Your current balance is {}.
        """.format(self.owner, self.balance)

myAccount = Account("Tom", 10000)
print(myAccount)