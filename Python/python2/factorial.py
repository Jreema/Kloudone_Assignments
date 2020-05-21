#program to find the factorial of a given number
x= int(input("Enter a number: "))
print(type(x))
def fact(num):
    if(num==1 or num==0):
        return 1
    else:
        return num * fact(num-1)
y = fact(x)
print(y)
