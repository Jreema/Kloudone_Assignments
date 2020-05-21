#swap position of two numbers in a list
list1=[78,90,34,23,12,67,56,77]
pos1 = int(input("Enter position1, number between 0 and 7:"))
pos2 = int(input("Enter position2, number between 0 and 7:"))
print("The original list is: ")
print(list1)
list1[pos1],list1[pos2] = list1[pos2],list1[pos1]
print("The swapped list is: ")
print(list1)