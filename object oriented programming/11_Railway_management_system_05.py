class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
        
        self.available_seats=set(range(1,seats+1))
        self.booked_seats = {}
        
        
    def getstatus(self):
        print("Train info:....\n")

        print(f"Train Name: {self.name}")
        print(f"Total Seats:{self.seats}")
        print(f"Available Seats: {len(self.available_seats)}")
        print(f"Booked_seats:{len(self.booked_seats)}")
        
    def fareinfo(self):
        print(f"Fare: {self.fare}")
        
    def bookticket(self,passanger_name):
        if (self.seats<=0):
            print("sorry the train is full")
        else:
           seat= min(self.available_seats)
           self.available_seats.remove(seat)
           self.booked_seats[seat]=passanger_name
            
    def cancleticket(self,seat_number):
        if seat_number in self.booked_seats:
           passanger =self.booked_seats.pop(seat_number)
           self.available_seats.add(seat_number)
           print(f"the ticket for {passanger} with {seat_number} is  cancelled")

        else:
            print(f" the ticket for seat {seat_number} is not booked")


    def booked_ticket(self):
        if not self.booked_seats:
            print("No tickets booked yet")
        else:
            for seat,passanger in sorted(self.booked_seats.items()):
                print(f"seat {seat}:{passanger}")


        
        
                
            
abhiyan=train('chennaiexpress',90,300)
choose= int(input("enter the respective number:\n"))

while True:
    print("Railway information:\n")
    print("1.Train status")
    print("2.fare info")
    print("3.Book Ticket")
    print("4.Cancle Ticket")
    print("5.Booked Ticket")
    print("5. Exit")


    

    if choose== 1:
        abhiyan.getstatus()

    elif choose== 2:
        abhiyan.fareinfo()

    elif choose== 3:
        name= input("enter passenger name:")
        abhiyan.bookticket(name)

    elif choose == 4:
        num= int(input("enter the ticet number to cancle:"))
        abhiyan.cancleticket(num)

    elif choose== 5:
        abhiyan.booked_ticket()

    elif choose == 6:
        print("Thank you for using my system.")

    else:
        print("invalid number")



    










