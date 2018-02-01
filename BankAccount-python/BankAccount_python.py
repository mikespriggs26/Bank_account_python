class Client():
    def __init__(self, first_name, last_name, account_number):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        
    
    def accountInfo(self):
        print ("Account owner: \t" + self.first_name + " " + self.last_name);
        print ("Account #: \t" + self.account_number);

    def Welcome(self):
        user_log_in = input("Welcome to Python Bank. Please enter your name to login: ")
        while user_log_in != self.first_name + " " + self.last_name:
            user_log_in = input("That is not the correct name on the account.  Please try again: ")

    def Goodbye(self):
        print("Thank you for banking with us.")
        raise SystemExit
            

class CheckingAccount():
    
    def __init__(self, checking_balance):
        self.checking_balance = checking_balance
    deposit_amount = 0
    def account_balance(self):
        print("Your checking account balance is $" + str(self.checking_balance))
    def make_checking_deposit(self):
        print("Your beginning balance is $" + str(self.checking_balance))
        self.checking_balance += self.deposit_amount
        print("You have deposited $" + str(self.deposit_amount))
        print("Your new checking account balance is $" + str(self.checking_balance))
    def make_checking_withdrawal(self):
        if checking_account.withdrawal_amount > self.checking_balance:
            self.checking_balance -= self.withdrawal_amount
            print("You have withdrawn $" + str(self.withdrawal_amount))
            print("Your new checking account balance is $" + str(self.withdrawal_balance))
        else:
            print("You do not have sufficient funds.  Please try again.")





class SavingsAccount():
    def __init__(self, savings_balance):
        self.savings_balance = savings_balance
    def account_balance(self):
        print("Your savings account balance is $" + str(self.savings_balance))







def main():
    customer = Client("John", "Smith", "1234")
    checking_account = CheckingAccount(5000)
    savings_account = SavingsAccount(1000)
    
    customer.Welcome()

    options_list = [];
    options_list.append("1. View Client Information")
    options_list.append("2. View Account Balance")
    options_list.append("3. Make a Deposit")
    options_list.append("4. Make a Withdrawal")
    options_list.append("5. Exit")
    for option in options_list:
        print(option)
    user_option = input("Please select a number from the list above and press enter:")
    if user_option == "1":
        customer.accountInfo()
    elif user_option == "2":
        account_info_input = input("View which account balance?  1. Checking  2. Savings")
        if account_info_input == "1":
            checking_account.checking_balance()
        elif account_info_input == "2":
            savings_account.savings_balance()
    elif user_option =="3":
        account_deposit_input = input("Into which account?  1. Checking  2. Savings")
        if account_deposti_input == "1":
            checking_account.deposit_amount = int(input("Enter deposit amount:"))
            checking_account.make_checking_deposit
    #while user_option != 5:
        
            
    #else:
    #    if user_option == "5":
    #        print("adsf")
    #        customer.Goodbye()


    #customer.accountInfo()
    #checking_account.account_balance()
    #savings_account.account_balance()

    #checking_account.deposit_amount =  int(input("Enter deposit amount:"))
    #checking_account.make_checking_deposit()

if __name__ == "__main__": main()