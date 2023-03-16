import welcome_screen as ws
import user_database as database
# Functions Dictionary
BANK_NAME = 'PyBank'
welcome_options = {
    1: ws.login,
    2: ws.new_user,
    3: ws.reset_password,
}
print(database.database)

onApp = True
while onApp:
    option = int(input(f'Hello, Welcome to {BANK_NAME} Choose one option.\n1. Login\n2. Register\n3. Reset Password\n'))

    if option < 0 or option >= 4:
        print('Invalid input.\n')
    else:
        onApp = False

welcome_options[option](BANK_NAME)

