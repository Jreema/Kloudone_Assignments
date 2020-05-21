#append() - adds an element to the end of the list
colors = ["red","yellow","orange"]
colors.append("blue")
print(colors)
#clear - clears the contents of a list
colors.clear()
print(colors)
#copy - copies the contents of one list to another
color =["red","blue","green"]
new_list = color.copy()
print(new_list)
#count - counts the number of times a specific items appear on the list
x= [1,1,6,2,8,1,2,9,1]
print(x.count(1))
#index - gives the index of the first occurance of an item in the list
print(x.index(2))
#insert - inserts an item at a specific index
fruits =["apple","orange","mango"]
fruits.insert(2,"banana")
print(fruits)
#pop - removes and returns the removed value as specified in the index
fruit =fruits.pop()
print(fruits, fruit)
#remove - removes the first occurance of a specific value in a list
a= [1,2,3,4,5,1,2,3,4,5]
a.remove(3)
print(a)
#reverse - reverses the order of elements in a list
a= [1,2,3,4,5]
a.reverse()
print(a)
#sort - sorts the array in ascending or descending order\
a=[100,700,300,400]
a.sort()
print("In ascending order: ",a)
a.sort(reverse=True)
print("In descending order: ",a)