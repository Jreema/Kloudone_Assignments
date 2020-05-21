import trip
car_dict = {"1":"Sedan","2":"Mini","3":"Limo","4":"Innova","5":"Indica","6":"UberShare"}
loop = True
trip_id=100
id1=0
st_trip = []
while(loop):
    choose_menu = input("Enter a choice:\t1. Book a Ride\t2. Calculate Fare & End a Ride\t3. Get Status of a Ride\t4. Exit\n")
    if(choose_menu not in ['1','2','3','4']):
        print("Invalid Input Given")
        exit(0)
    if choose_menu=='1':
        car_choice= input("Choose a car:\t1.Sedan\t2.Mini\t3.Limo\t4.Innova\t5.Indica\t6.UberShare\n") 
        if car_choice not in ['1','2','3','4','5','6']:
            print("Invalid Choice Entered")
            exit(0)
        start = input("Enter Starting Place: ")
        stop = input("Enter Destination: ")
        st_trip.append(trip.Main_trip(trip_id,start,stop))
        st_trip[id1].choose_car(car_dict[car_choice])
        print("Your trip has started")
        print("Your trip id is: ",st_trip[id1].id)
        id1 += 1
        trip_id +=1
        c=input()
    elif choose_menu =='2':
        query_id1 = int(input("Enter the trip id: "))
        id2 = query_id1-100
        dist =int(input("Enter the distance travelled: "))
        st_trip[id2].car.set_distance(dist)
        print("Your Trip id is: %d"%(st_trip[id2].id))
        print("Vehicle used: "+st_trip[id2].car.car_type)
        print("Your Starting Place: "+ st_trip[id2].start)
        print("Your Destination: "+ st_trip[id2].destination)
        print("Your fare is: Rs.",end='')
        print(st_trip[id2].car.fare())
        st_trip[id2].end_ride()
        print("Ride Ended")
        c=input()
    elif choose_menu=='3':
        query_id2 = int(input("Enter your Trip id: "))
        id3 = query_id2 -100
        print("The vehicle is: "+st_trip[id3].car.car_type)
        print("The Starting Place of your ride is: "+st_trip[id3].start)
        print("The Destination of your ride is: "+st_trip[id3].destination)
        print("The Status of your ride is: "+st_trip[id3].status)
        c =input()
    else:
        loop = False
