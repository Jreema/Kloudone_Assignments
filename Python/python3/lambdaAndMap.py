#to multiply all elemnts in a list by a number using map and lambda function
str1 =input("Enter the elements of an array separated by space: ")
my_list = list(str1.split(" "))
print(my_list)
i =int(input("Enter the number to be multiplied: "))
#result=[int(num)*2 for num in my_list]
def mul(list1,iter1):
    return (list(map(lambda num: int(num)*iter1, list1)))

result=mul(my_list,i)
print(result)