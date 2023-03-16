# Second screen functions

# import transfer functions
import home_options as op

options = {
    1: op.deposit,
    2: op.withdraw,
    3: op.transfer_type,
    4: op.buy_airtime
}

account_balance = 0.00


def welcome(user='User', bank_name='PyBank'):
    print("Printing from home screen\n")
    print(f'Welcome {user}.\nYour {bank_name} account balance:{account_balance}.\nYour can perform any of these.\n')


def home(bank_name):
    option = int(input('1. Deposit\n2. Withdraw\n3.Transfer\n4. Buy Airtime\n'))
    if option <= 0 or option >= 5:
        print("Invalid input")
        home(bank_name)
    else:
        options[option](account_balance)
