#program to remove duplicate characters in a string
str = input("Enter a string: ")
set1="".join(dict.fromkeys(str))
print(set1)