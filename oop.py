# class
#     1. data or property
#     2. functionc or behaviour

# Systax to create an object
# objectname = classname()




#------------ATM class------------

# Ques:-> Whas is the true value of Constructor?
# Ans: jo bhi configuration wale task hai wo. jo bhi task jo aap usr ke bin apooche krna chahte ho 
#        us constructor ke andar rakhte 
    #    - Automatically called when object is created

# Types of constructor 

# 1. Default constructor:   
#     Takes no Parameter , set default values.

# example:     class ATM {
# public:
#     ATM() {
#         cout << "ATM Created";
#     }
# };

# 2. Parameterized constructor :
#     Takes parameter , used to intialize value at object creation

# example :  class Account {
# public:
#     int balance;

#     Account(int b) {
#         balance = b;
#     }
# };


class Atm:
    def __init__(self):
    #__init__ -> constructor : kisi object k attributes ko intialize krne k liye use kiya jata hai.
    # attributes -> properties hoti ho jo kisi object ya class ke andar stored hote hai. Here->pin,balance
        self.pin = ''
        self.balance = 0
        self.menu()
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
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            print('your balance is', self.balance)
        else:
            print('chal nikal yaha se')
        
    def withdraw(self):
        user_pin == input('enter the pin')
        if user_pin == self.pin:
            # allowed to withdraw
            amount = int(input('Enter the amount'))
            if amount<self.balance:
                self.balance = self.balance - amount
                print
        else:
            print("you are not eligible to do this.")




# Ques: -> Write OOP classes to handle the following scenarios.
#         1. A user can create and view 2D coordinates.
#         2. A user can find out the distance between 2 coordinators 
#         3. A user can find out the distance of a coordinate from origin
#         4. A user can check if a point lies on a given line.
#         5. A user can find the distance between a given 2D point and a given line.



class Point:
    # self is default parameter
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{}{}>' .format(self.x_cod,self.y_cod)     # ye print krne ke liye hai example: <3,4>

    def eucledian(self,other):
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return (self.x_cod**2 )
        return self.eucledian_distance(self,Point(0,0))

class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)      # l1 = Line(2,3,4)    
    
    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:   
            return "Points lies in the line"
        else:
            return "Points does not lies on the Line."
        
        
# Refrence Variables

class Person:

    def __int__(self):
        self.name = "Nitish"
        self.gender = "Male"

p = Person()    # p ek reference variable hai jiske pass address hai object ka.
print(id(p))
p1=greet(p)
print(id(p1))



# Encapsulation 
