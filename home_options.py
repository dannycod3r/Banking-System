import transfer as tr


def deposit(account_balance=0):
    pass


def withdraw(account_balance=0):
    pass


def transfer_type(account_balance=0):
    print(account_balance)
    options = {
        1: tr.domestic,
        2: tr.other_local_banks,
        3: tr.international_transfer,
        4: tr.mobile_money
    }
    option = int(input('Select transfer type:\n1. Domestic\n2. Other Local Bank\n3. International Transfer\n4. Mobile '
                       'Money Transfer'))
    if option <= 0 or option >= 5:
        print('Invalid input')
        transfer_type(account_balance)
    else:
        options[option](account_balance)


# When user want to buy airtime
def buy_airtime(account_balance=0):
    print(account_balance)
    # Variables tha I will use
    sentence = 'Enter beneficiary number: '
    balance = account_balance
    network = 0
    num = '0'

    # Function responsible for checking account balance against amount of airtime to purchase
    def finish_purchasing(number, balanc,):
        amount_to_purchase = int(input('Enter the amount: '))
        if balanc - amount_to_purchase > 0:
            return f'You have successfully purchased Gh{amount_to_purchase} of airtime on the number {number}.'
        else:
            return 'Insufficient account balance'

    # Check the validity of inputted number
    def number_len(number):
        if len(number) != 10:
            print('Invalid number')
        else:
            print(finish_purchasing(number=num, balanc=balance))

    # Check for correct network operator
    choose_operator = True
    while choose_operator:
        network = int(input("Select Network operator:\n1. MTN\n2. AirtelTigo\n3. Vodafone\n"))
        if network < 1 or network >= 4:
            print('Invalid selection')
        else:
            num = (input(f'{sentence}(e.g:024xxxxxxx) '))
            number_len(number=num)
            choose_operator = False
