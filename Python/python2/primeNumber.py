# To check whether a number is prime number or not
x =input("Enter a number: ")
x =int(x)
if(x>1):
    for i in range(2,x//2+1):
        if(x%i==0):
            print("Not a Prime Number")
            break
    else:
        print("Is a prime Number")
else:
    print("Not a prime Number")
