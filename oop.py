# class
#     1. data or property
#     2. function or behaviour

# Systax to create an object
# objectname = classname()





Ques:-> Whas is the true value of Constructor?
Ans: jo bhi configuration wale task hai wo. jo bhi task jo aap usr ke bin apooche krna chahte ho 
       us constructor ke andar rakhte 
       - Automatically called when object is created

Types of constructor 

1. Default constructor:   
    Takes no Parameter , set default values.

# example:     
class ATM {
    public:
        ATM() {
            cout << "ATM Created";
        }
}

2. Parameterized constructor :
    Takes parameter , used to intialize value at object creation

example :  class Account {
public:
    int balance;

    Account(int b) {
        balance = b;
    }
};


# Jab bhi static variable ko use krte ho to class ka naam lekr use krte hai.
# jab bhi  instance variable ko use krte hai to object ka naam lekr use krte hai.

# Example:

class Atm:
    __counter = 1
    def __init__(self):
        print(id(slef))
        self.pin = ''
        self.__balance = 0
        self.cid = Atm.__counter + 1   # here we use staic and instance variable 








#------------ATM class------------


class Atm:
    def __init__(self,account_number,pin,balance=0):
    #__init__ -> constructor : kisi object k attributes ko intialize krne k liye use kiya jata hai.
    # attributes -> properties hoti ho jo kisi object ya class ke andar stored hote hai. Here->pin,balance
        self.account_number=account_number
        self.__pin = pin         # Private attribute bnane ke liye use kiya hai __ (Encapsulation) 
        self.__balance = balance

    def __verify__pin(self,pin):        
        # ye method sirf class ke andar hi use kr skte hai (Private method)
        return self.__pin == pin

    def check_balance(self,pin):
         # Abstraction -> user ko sirf balance dekhna hai pin check krne ka logic hide hai
        if self.__verify__pin(pin):
            print(f"Account{self.account_number} -> Balance:{self.__balance}")
        else:
            print("Incorrect pin")

    def deposit(self,amount,pin):
       
        if self.__verify__pin(pin):
            if amount>0:
                self.__balance +=amount
                print(f"{amount} deposited. New amount {self.__balance}")
            else:
                print("deposit must be positive")
        else:
            print("Incorrect Pin")


    def withdraw(self,amount,pin):
        # Polymorphism ke liye ye method child classes override kr sakti hai (CurrentAccount me)
        if self.__verify__pin(pin):
            if amount < self.__balance:
                self.__balance -= amount
                print(f"{amount} withdrawn, Remaining Balance {self.__balance}")
            else:
                print("Insufficient amount")
        else:
            print("Incorrect pin")

    def _get_balance(self):       # getter (Encapsulation) -> indirectly data ko access krne ka way
        return self.__balance
    
    def _set_balance(self,value):    #setter (Encapsulation) -> indirectly data ko modify krne ka way
        self.__balance = value
 
class SavingAccount(ATM):
    def __int__(self, account_number, pin, balance=0, overdraft_limit=0):
        super().__init__(account_number, pin, balance)
        # super() -> iska use parent class ki properties 
        





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




