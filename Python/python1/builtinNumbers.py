import math
import random
#abs() returns the absolute value of a number
x=9
print("The absolute value of %d: %d" %(x,abs(x)))
x=-78
print("The absolute value of %d: %d" %(x,abs(x)))
x=complex(19,25)
print("The absolute value of : %f" %(abs(x)))
# ceil() rounds a number to the nearest higher integer
x=8.3
print("The ceil of %d: %d" %(x,math.ceil(x)))
# floor() rounds a number to the nearest lowest integer
x=8.3
print("The floor of %d: %d" %(x,math.floor(x)))
#exp() gives the e power x (Exponential of x)
x=45.7
print("The exponential of %f is: %f"%(x, math.exp(x)))
#log() gives the natural logarithm of a number
x=100
#log10() gives the 10 base logarithm of a number
print("The natural logarithm of %d is: %f"%(x, math.log(x)))
x=100
print("The 10 base logarithm of %d is: %f"%(x, math.log10(x)))
# max() returns the maximum of the paramenters
x,y,z = 45, 90, 21
print("The maximum of %d, %d, %d is %d"%(x,y,z,max(x,y,z)))
#min() returns the minimum of the given paramenters
x,y,z = 45, 90, 21
print("The minimum of %d, %d, %d is %d"%(x,y,z,min(x,y,z)))
#all() checks if all items in a list or set or tuple or dictionary are true
list1=[9,0,True]
print("The items in the list are true: "+ str(all(list1)))
#any() checks if any of the items in a list or set or tuple or dictionary is true
dict1={0:"zero",1:"one", 2:"two"}
print("Any items in the dictionary is true: "+ str(any(dict1)))
#bin() returns the binary version of a number
x=36
print("The binary of %d is: "%(x) +bin(x))
#bool() returns the boolean value of the specified object
x="any string"
print("The boolean of x is "+ str(bool(x)))
#callable() returns true if the object is callable otherwise returns false
x=9
print("Is x=9 callable? "+str(callable(x)))
#dict() creates a dictionary with the paramenters given
colors = dict(c1="Orange",c2="red",c3="purple",c4="blue",c5="yellow")
print(colors)
#divmod() gives a tuple which is the quotient and remainder obtained by dividing parameter1 by paramenter2
print(divmod(9,5))
#enumerate() - returns an enum of the given collection starting at the index mentioned as 2nd parameter
print(list(enumerate(("Orange","Cherry","Banana"),2)))
#eval() - Evaluates and executes an expression 
x="print(50)"
eval(x) 
#float() converts a number into floating point number
x =float(8)
print(x) 
#int() - returns an integer number
x=3.5
print(int(x)) 
#pow() - returns the value of x to the power of y
print(pow(2,5))
#round() - returns the round of the given number to the corresponding decimal points(optional)
print(round(100.96753,2)) 
#sqrt() - returns the square root of a number greater than 0
print(math.sqrt(81)) 
#choice() returns a random item from a sequence
x=[1,2,3,4,5,6]
print(random.choice(x)) 
#randrange()- gives a random number in the range
print(random.randrange(5,9,1)) 
#random() - gives a random number between 0 and 1. (excluding 1 and including 0)
print(random.random()) 
#shuffle() - returns a reordered or reshuffled list of the items
y=[10,20,30,40,50]
random.shuffle(y)
print("Reshuffled list is : ",y) 