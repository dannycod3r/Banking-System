def mobile_money(account_balance=0):
    # Variables tha I will use
    sentence = 'Enter beneficiary number: '
    amount_in_account = account_balance

    # Function responsible for checking account balance against amount of airtime to purchase
    def confirm_transaction(number, balance):
        beneficiary_name = input('Receiver account name: ')
        amount_to_send = int(input('Enter the amount: '))
        if balance - amount_to_send > 0:
            return f'You have successfully sent Gh{amount_to_send} to {beneficiary_name} on {number}.'
        else:
            return 'Insufficient account balance'

    # Check the validity of inputted number
    def number_len(number):
        if len(number) != 10:
            print('Invalid number')
        else:
            print(confirm_transaction(number=num, balance=amount_in_account))

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


def domestic(account_balance=0):
    pass


def other_local_banks(account_balance=0):
    pass


def international_transfer(account_balance=0):
    pass
