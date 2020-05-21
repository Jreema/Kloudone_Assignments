#Calculator
x = int(input("Enter the frist number: "))
y = int(input("Enter the second number: "))
c =int(input("Enter a number:\n 1 Additon\n2 Subtraction\n3 Multiplication\n4 Division\n"))

def calculate(num1,num2,choice):
    if choice == 1:
        print(add(num1,num2))
    elif choice==2:
        print(sub(num1,num2))
    elif choice==3:
        print(mul(num1,num2))
    elif choice==4:
        print(div(num1,num2))
    else:
        print("Not a valid Choice.")

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

calculate(x,y,c)