class BankAccount:
    def __init__(self, account_number,accounts_name, account_type, balanace = 0):
        self.account_number = account_number
        self.accounts_name = accounts_name
        self.account_type = account_type
        self.balance = balanace
        self.transaction_history = []

    def deposit(self,amount):
        self.balance += amount
        self.transaction_history.append(f"You deposited{amount}")
        return 'Successful'
    
    def withdraw(self,amount):
        if amount > self.balance:
            return 'Insufficient Funds'
        self.balance -= amount
        self.transaction_history.append(f'You withdrew{amount}')
        return 'Successful'
    
    def get_statement(self):
        for transactions in self.transaction_history:
            print(transactions)


    def check_balance(self):
        return self.balance
    
    

def main():
    accounts = []
    while True:
        print('Select an option')
        print('1. Create an account')
        print('2. Deposit funds to your account')
        print('3.Withdraw funds from your account')
        print('4.Get balance')
        response = int(input(''))

        if response == 1:
            name = input('Enter your name')

            print('select an account type')
            print('1. savings')
            print('2. current')
            print()
            account_response = int(input(''))
            if account_response ==1:
                account_type = 'savings'
            elif account_response ==2:
                account_type = 'current'    

            initial_deposit = int(input('deposit an amount'))
            account_number= 12345678
            new_account = BankAccount(account_number, name, account_type, initial_deposit)
            accounts.append(new_account)   
            print(f"account created! your account number is {account_number}")
        elif response == 2:
            name = input('Enter your name')    
            for account in accounts:
                if account.accounts_name == name:
                   amount =  int(input('Please enter amount: '))
                   print(account.deposit_funds(amount))
                   break
            else:
                print("Can't find your account")
        elif response ==3:
            name = input('Enter your name')
            for account in accounts:
                if account.accounts_name == name:
                    amount = int(input('Please enter amount to withdraw: '))
                    print(account.withdraw_funds(amount))
                    break
            else:
                print("Can't find your account" )    
        elif response == 4:
            name = input('Enter your name')        
            for account in accounts:
                if account.accounts_name == name:
                    print (account.check_balance)

main()

            


        