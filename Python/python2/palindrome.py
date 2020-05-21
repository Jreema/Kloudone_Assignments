#Check if  a number is palindrome or not
x = input("Enter a number: ")
y =x[::-1]
if(x==y):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")