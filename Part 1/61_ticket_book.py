class RailwayTicket:
    def __init__(self, name, price, seat):
        self.name = name
        self.price = price
        self.seat = seat

    def getStatus(self):
        print(f"Name of train is {self.name}")
        print(f"No. of seats is {self.seat}")

    def fareInfo(self):
        print(f"Price of ticket is ₹{self.price} per seat")

    def bookTicket(self):
        if(self.seat>0):
            print(f"Your ticket has been booked successfully\nYour seat no. is {self.seat}")
            self.seat-=1
        else:
            print("Train seats are full, try Tatkal")
            
    def cancelTicket(self):
        self.seat+=1
        print("Ticket has been cancelled, refund will be processed shortly")
        
Metro1 = RailwayTicket("Green Line", 35, 2)

Metro1.getStatus()
Metro1.fareInfo()

Metro1.bookTicket()
Metro1.getStatus()

Metro1.bookTicket()
Metro1.getStatus()

Metro1.bookTicket()
Metro1.getStatus()

Metro1.cancelTicket()
Metro1.getStatus()

