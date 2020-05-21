from functools import reduce
str1 =input("Enter the elements separated by a space: ")
list1 = list(str1.split(' '))
result= reduce(lambda x,y: int(x)+int(y), list1)
print(result)