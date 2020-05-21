#add() - adds an element to the set if it doesnot already exists in the set
x = {"apple", "banana", "cherry"}
x.add("orange")
print(x) 
#difference() - returns the elements in first set which are not in the second set into a new set
x = {1, 2, 3}
y = {3, 4, 5}
z = x.difference(y)
print(z) 
#difference_update() - updates the first set by deleting the contents in the second set which are present in first set
x = {1, 2, 3}
y = {3, 4, 5}
x.difference_update(y)
print(x)
#union - Gives the union of two sets
x={1,2,3}
y={3,4,5}
z=x.union(y)
print(z)
#intersection - Gives the intersection of two sets
x={1,2,3}
y={3,4,5}
z=x.intersection(y)
print(z)
#update - updates the current set by adding items from second set not present in first set
x={1,2,3}
y={3,4,5}
z=x.update(y)
#discard - removes the item from the set
fruits= {"apple","banana","mango"}
fruits.discard("apple")
print(fruits)