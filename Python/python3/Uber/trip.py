#imports the various cars from uberCars
from uberCars import Sedan,Mini,Limo,Innova,Indica,UberShare

class Main_trip:
    #constructor assigns the id, starting place and destination of the trip.
    def __init__(self,ident,start,stop):
        self.id = ident
        self.start = start
        self.destination = stop
        self.status = "In Progress"
    
    #Creates an object by callling the appropriate subclass of car object
    def choose_car(self,car_name):
        str1= car_name + "()"
        self.car= eval(str1) #evaluates the expression
    
    #updates the status of the ride
    def end_ride(self):
        self.status ="Ride Ended"

