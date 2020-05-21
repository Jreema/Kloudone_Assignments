#to generate fibonacci series until a particular number using Generators
max_number = int(input("Enter the maximum number in the series: "))

def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
    
out = fib()
for i in out:
    if i> max_number:
        break
    print(i,end="\t")