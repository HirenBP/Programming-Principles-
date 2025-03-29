class GoCardAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []
        self.transactions.append(('Initial balance', 0, self.balance))

    def ride(self, amount):
        self.balance -= amount
        self.transactions.append(('Ride', amount, self.balance))

    def top_up(self, amount):
        self.balance += amount
        self.transactions.append(('Top up', amount, self.balance))

    def get_balance(self):
        return self.balance

    def print_statement(self):
        print('Statement:')
        print('event\t\t\t\tamount ($)\tbalance ($)')
        for event, amount, balance in self.transactions:
                if event == 'Initial balance':
                    print(f'{event}\t\t\t\t\t{balance:.2f}')
                    continue

                print(f'{event}\t\t\t\t{amount:.2f}\t\t{balance:.2f}')
        print('Final balance\t\t\t\t\t{:.2f}'.format(self.balance))

if __name__ == '__main__':
    account = GoCardAccount(int(input('Creating account. Input initial balance: ')))
    command = input('?').split()
    while command[0] != 'q':
        if command[0] == 'r' and len(command) == 2:
            account.ride(float(command[1]))
        elif command[0] == 'b':
            print('Balance: {:.2f}'.format(account.get_balance()))
        elif command[0] == 't' and len(command) == 2:
            account.top_up(float(command[1]))
        else:
            print('Bad input')
        command = input('?').split()
    account.print_statement()

