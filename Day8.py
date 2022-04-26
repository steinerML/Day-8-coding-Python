#Functions in Python
#We define the function by using function definition *def()*
def greet ():
    print("Hello")
    print("How do you do?")
greet()
print("So this is how you call a function!")

#Another upgraded function that also greets people.

def greet2 (name):
    print("Hello",name)
    print("How are you doing",name,"?")

greet2("James")

#Same function but with multiple arguments!

def greet3 (name, age):
    print("Hello",name)
    print("Welcome",name,"according to our records you are",age)

greet3("Peter", 33)

#Another function passing multiple arguments

def add_numbers(n1,n2):
    result = n1 + n2
    print("The total sum is", result)

number1 = 5.65
number2 = 6.35

add_numbers(number1,number2)

#Return a value from a function

def add_numbers(n1,n2): #Function starts here and it executes (2)
    result = n1 + n2
    return result #Function is returned to (1)

number0 = 9.94
number1 = 8.65

result = add_numbers(number1,number2) #We call w/ 2 arguments (1)
print("The total result is",result)