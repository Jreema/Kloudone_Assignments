#capitalise() -capitalises the first letter of a string
x="first letter is capitalised"
y =x.capitalize()
print(y)
#casefold() - changes  astring into lower case
x="Hello, How are YOU?"
y=x.casefold()
print(y)
#center() - aligns the string on the screen
x="hello world"
print(x.center(20,'*'))
#count() - returns the number of times a substring appears in a string
x="I am going to the zoo"
print(x.count('o'))
#endswith() - returns true if a string ends with a particular value
x="Integer"
print(x.endswith("er"))
#find() - returns the index of the substring in a given string returns -1 if string not found
x="Hello world how is the world"
print(x.find('world'))
#index() - similar to find() method, but raises an exception is string not found
x="Hello how r you"
print(x.index('l')) 
#isalnum - returns true if the string contains only alphanumeric values
x="half05"
print(x.isalnum())
#isalpha - returns true if the string contains only alphabets
x="What is the Time Now"
print(x.isalpha())
#isdigit - returns true if the string contains only digits
x="98760"
print(x.isdigit())
#islower - returns true if all chars in a string are lower case
x="This Will give false"
print(x.islower())
#isupper - returns true if all chars in a string are upper case
x="THIS IS TRUE"
print(x.isupper()) 
#join() - joins the iterable by the separator given
x=("Apple","Orange","Mango","Banana")
print('**'.join(x))
#lower - converts the string to lowercase
x="You are my FRIEND"
print(x.lower())
#upper - converts the string to upper case
x="i cannot fly"
print(x.upper())
#replace - replaces a substring with the given string
x="i am sleepy i am hungry"
print(x.replace("i am","you are"))
#strip - deletes the whitespace around a string
x="  Hello Trim Me Please   "
print(x.strip())