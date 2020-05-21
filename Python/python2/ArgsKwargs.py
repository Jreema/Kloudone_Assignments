#*args - variable argument list - tuple is passed
def addition(*num):
    x =sum(num)
    return x

print(addition(90,67,45))

#**kwargs - keyword arguments - dictionary is passed
def my_function(**car):
  print("The make of the car is " + car["make"])
  print("The model of the car is "+ car["model"])

my_function(make = "Hyundai", model = "I30") 