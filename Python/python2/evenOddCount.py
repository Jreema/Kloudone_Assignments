# to count the number of even and odd numbers in a list 
list1 = [100, 213, 40, 453, 660, 931, 115] 
odd_count = len(list(filter(lambda x: (x%2 != 0) , list1))) 
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))
print("Even numbers in the list: ", even_count) 
print("Odd numbers in the list: ", odd_count) 
