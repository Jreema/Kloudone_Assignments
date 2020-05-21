#to check if a number is armstrong number or not
x=input("Enter a number: ")
x= x.lstrip('0')
order = len(x)
number = list(x)
out = [int(num)**order for num in number]
total =sum(out)
if total== int(x):
    print(x," is an armstrong number")
else:
    print(x," is not an armstrong number")