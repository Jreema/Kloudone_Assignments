from functools import reduce
str1="hello"
print(list(str1))
print(tuple(str1))
print(set(str1))
list1=["5","6","7"]
print(str(list1))
var = "".join(list1)
print(var)
list2 = [9,8,7]
var1 = "".join([str(elm) for elm in list2])
print(var1)