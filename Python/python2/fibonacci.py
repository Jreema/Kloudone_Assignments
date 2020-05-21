#print the fibonacci series for a given number
x = int(input("Enter a number: "))
result=[0,1]
def fib_series(num):
    global result
    if num<=0:
        print("Enter a valid input")
        exit(0)
    elif num==(1 or 2):
        pass
    else:
        for i in range(num-2):
            result.append((result[i]+result[i+1]))
fib_series(x)
for fib in result:
    print(fib,end=" ")