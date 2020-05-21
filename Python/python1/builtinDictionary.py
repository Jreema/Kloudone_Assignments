#items - returns the items in a dictionary as a view object
car = {
  "brand": "Fiat",
  "model": "Premier Padmini",
  "year": 1960
}
x = car.items()
print(x) 
#keys - returns the keys of the dictionary as a view object
car = {
  "brand": "Fiat",
  "model": "Premier Padmini",
  "year": 1960
}
x = car.keys()
print(x) 
#values() - Returns the values of a dictionary as a view object
car = {
  "brand": "Fiat",
  "model": "Premier Padmini",
  "year": 1960
}
x = car.values()
print(x) 
#get() - Returns the value of the item specified by the key
car = {
  "brand": "Fiat",
  "model": "Premier Padmini",
  "year": 1960
}
x = car.get("year")
print(x) 
#update() - inserts a specified value into the dictionary
car = {
  "brand": "Fiat",
  "model": "Premier Padmini",
  "year": 1960
}
car.update({"color": "Maroon"})
print(car) 