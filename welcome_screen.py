# All functions here

# External imports
import user_database as db
import home_screen
username = ''


# User Login
def login(bank_name):
    """Take user to login page"""
    global username
    correct_details = False
    count = 5
    while count > 0:
        print(f'Login into your {bank_name} account\n')
        username = input("Enter username: ").title()
        password = input('Enter pincode: ')
        # Check if user details is in the database
        for key, value in db.database.items():
            if username == value['first_name']:
                print('Printing key: ')
                print(value['first_name'])
                correct_details = True

        if correct_details:
            break
        else:
            count -= 1
            print(count)

    if count > 0:
        user = db.user(username)
        home_screen.welcome(user)
        home_screen.home(bank_name)
    # Lock user out and ask for password reset if they enter wrong password more than 3 times
    if count == 0:
        print("""
You have entered wrong details more than 3 time.
Your are locked out of your account.
        """)
        reset_password(bank_name)


# Register new user
def new_user(bank_name):
    """register new users"""
    global username
    # Take user details
    print(f"Please fill out this form to create a {bank_name} account\n")
    user_name = input("Fullname: ").title()
    user_dob = int(input('Enter your date of birth(DD/MM/YYYY): '))

    account_selection = True
    while account_selection:
        account_type = int(input('Account type\n1. Savings account\n2. Current account\n'))
        if account_type == 2:
            confirm_account_type = True
            print("You'll be charged Ghc10.00 every month as maintenance fee.")
            while confirm_account_type:
                option = int(input('1. Continue\n2. Go back\n'))
                if option == 1:
                    confirm_account_type = False
                    account_selection = False
                elif option == 2:
                    confirm_account_type = False
                    account_selection = True
                else:
                    confirm_account_type = True
        elif account_type == 1:
            account_selection = False
        else:
            print('Invalid Selection')
            account_selection = True

    email = input('Enter your email address: ')
    username = input('Setup a username: ')
    password = int(input('Enter a 6 digit pincode: '))
    print(f'Welcome {username}.\nYour {bank_name} pincode is {password}, keep it safe.\n')

    # Save user details - User database later
    db.database[username] = password
    user = db.user(username)
    home_screen.welcome(user, bank_name)
    home_screen.home(bank_name)


# Reset user password
def reset_password(bank_name):
    """help user reset password"""
    print(f"""
Fill this form to reset your {bank_name} password
    """)
    user = input("Enter your username: ")
    email = input('Enter your email: ')
    # send email to user
