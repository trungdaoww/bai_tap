class Bank:
    Account_type = "Saving"
    location = "Guntur"
    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location

    def __repe__(self):
        print("Welcome to the BIDV ATM Machine")
        print("-"*20)
        account_pin = int(input("Please enter your pin number"))
        if(account_pin==123):
            Account(self):
                
