class Train:
    def __init__(self,myName,name,fare,seats):
        self.myName = myName
        self.name = name
        self.fare =fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"Available seats in this train is {self.seats}")
        print("*********")
    def bookTickets(self):
        if(self.seats>0):
            print(f"Dear {self.myName}, your Ticket has been booked!. Your Seat No. is {self.seats}")       
            print("*********")
            self.seats = self.seats - 1
        else:
            print("Sorry, This train is Full. Try in Tatkal(Emergency)")
            print("*********")

    def fareInfo(self):
        print(f"The price of the ticket is {self.fare}")
        print("*********")


journey = Train("Sahil","Rajdhani", 200, 150)

journey.getStatus()
journey.fareInfo()
journey.bookTickets()
journey.getStatus()

journey.myName="ayush"

journey.bookTickets()
journey.getStatus()