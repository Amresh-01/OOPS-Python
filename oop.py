# class
#     1. data or property
#     2. functionc or behaviour

# Systax to create an object
# objectname = classname()




#------------ATM class------------
class Atm:
    def __init__(self):
    #__init__ -> constructor : kisi object k attributes ko intialize krne k liye use kiya jata hai.
    # attributes -> properties hoti ho jo kisi object ya class ke andar stored hote hai. Here->pin,balance
        self.pin = ''
        self.balance = 0
        print('i am executed')

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw.
        5. Anything else to exit.
        """)
if user_input == '1':
    # create pin
    pass
elif user_input == '2':
    # change pin
    pass
elif user_input == '3':
    # check balance
    pass
elif user_input == '4':
    # withdraw
    pass
else:
    exit()

    def create_pin(self):
        user_pin = input('enter your pin')
        self.pin=user_pin

        user_balance = int(input('enter balance'))
        self.balance = user_balance

        print('pin created successfully')
    
    def change_pin(self):
        old_pin = input('enter old pin')

        if old_pin == self.pin:
            new_pin = input('enter new pin.')
        
        else:
            print('you are not elgible to che=ange the pin')
            self.menu()
    
    def check_balance(self):
        usr_
