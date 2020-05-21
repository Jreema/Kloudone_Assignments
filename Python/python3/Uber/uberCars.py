class Car:
    """ Car is the baseclass. It contains a method to calculate the fare. Car types derive from this class"""
    def __init__(self):
        pass
    speed = 0
    distance_covered =0
    rate =0
    #function to set the distance travelled
    def set_distance(self,dist):
        self.distance_covered=dist
    #function to calculate fare
    def fare(self):
         return self.rate*self.distance_covered
    
class Sedan(Car):
    """Car Type is Sedan. Subclass of Car. Has a rate of Rs.12 per Km"""
    car_type ="Sedan"
    def __init__(self):
        print("Sedan has been alloted to you.")
        self.rate= 12
        self.speed=40

class Mini(Car):
    """Car Type is Mini. Subclass of Car. Has a rate of Rs.10 per Km"""
    car_type ="Mini"
    def __init__(self):
        print("Mini has been alloted to you")
        self.rate= 10 
        self.speed=40
        
class Limo(Car):
    """Car Type is Limousine. Subclass of Car. Has a rate of Rs.35 per Km"""
    car_type ="Limousine"
    def __init__(self):
        print("Limo has been alloted to you")
        self.rate= 35
        self.speed=40

class Innova(Car):
    """Car Type is Innova. Subclass of Car. Has a rate of Rs.24 per Km"""
    car_type ="Innova"
    def __init__(self):
        print("Innova has been alloted to you")
        self.rate= 24
        self.speed=40

class Indica(Car):
    """Car Type is Indica. Subclass of Car. Has a rate of Rs.12 per Km"""
    car_type ="Indica"
    def __init__(self):
        print("Indica has been alloted to you")
        self.rate= 12
        self.speed=40

class UberShare(Car):
    """Car Type is UberShare. Subclass of Car. Has a rate of Rs.5 per Km"""
    car_type ="UberShare"
    def __init__(self):
        print("UberShare has been alloted to you")
        self.rate= 5
        self.speed=40

