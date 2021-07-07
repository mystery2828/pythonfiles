class Taxi:
    taxicount = 0
    def __init__(self):
        self.id = Taxi.taxicount
        Taxi.taxicount += 1
        self.currentSpot = 1
        self.booked = False
        self.freeTime = 6
        self.totalEarnings = 0
        self.trips = []
    
    def _print_info(self):
        print(self.id)
        print(self.currentSpot)
        print(self.booked)
        print(self.totalEarnings)
        print(self.trips)

    def setDetails(self,booked,currentSpot,freeTime,totalEarnings,trips):
        self.booked = booked
        self.currentSpot = currentSpot
        self.freeTime = freeTime
        self.totalEarnings = totalEarnings
        self.trips.append(trips)
    
    def printDetails(self):
    
        print("Taxi - "+ str(self.id) + " Total Earnings - " + str(self.totalEarnings))
        print("TaxiID    BookingID    CustomerID    From    To    PickupTime    DropTime    Amount")
        print(f"length {self.trips}")
        for trip in self.trips:
            print(trip)
        
        print("--------------------------------------------------------------------------------------")
    

    def printTaxiDetails(self):
        print("Taxi - "+ str(self.id) + " Total Earnings - " + str(self.totalEarnings) + " Current spot - " + str(self.currentSpot) +" Free Time - " + str(self.freeTime))
    

class Booking(Taxi):

    taxis = []
    def getFreeTaxis(self,taxis, pickupTime, pickupPoint):
            freeTaxis = []
            for t in taxis:
                if(t.freeTime <= pickupTime and (abs((t.currentSpot - 0) - (pickupPoint - 0)) <= pickupTime - t.freeTime)):
                    freeTaxis.append(t)
            return freeTaxis
        
    def bookTaxi(self,customerID, pickupPoint, dropPoint, pickupTime,freeTaxis):
        
        # // to find nearest
        min = 999

        # //distance between pickup and drop
        distanceBetweenpickUpandDrop = 0

        # //this trip earning
        earning = 0

        # //when taxi will be free next
        nextfreeTime = 0

        # //where taxi is after trip is over
        nextSpot = 7

        # # //booked taxi
        # Taxi bookedTaxi = null

        # //all details of current trip as string
        tripDetail = ""
        
        for t in freeTaxis:
        
            distanceBetweenCustomerAndTaxi = abs((t.currentSpot - 0) - (pickupPoint -0)) * 15
            if(distanceBetweenCustomerAndTaxi < min):
            
                bookedTaxi = t
                # //distance between pickup and drop = (drop - pickup) * 15KM
                distanceBetweenpickUpandDrop = abs((dropPoint - 0) - (pickupPoint - 0)) * 15
                # //trip earning = 100 + (distanceBetweenpickUpandDrop-5) * 10
                earning = (distanceBetweenpickUpandDrop-5) * 10 + 100
                
                # //drop time calculation
                dropTime  = pickupTime + distanceBetweenpickUpandDrop/15
                
                # //when taxi will be free next
                nextfreeTime = dropTime

                # //taxi will be at drop point after trip
                nextSpot = dropPoint

                # // creating trip detail
                tripDetail = (str(customerID) + "               " + str(customerID) + "             " + str(pickupPoint) +  "           " + str(dropPoint) + "          " + str(pickupTime) + "            " +str(dropTime) + "              " + str(earning))

        # //setting corresponding details to allotted taxi
        bookedTaxi.setDetails(True,nextSpot,nextfreeTime,bookedTaxi.totalEarnings + earning,tripDetail)
        # //BOOKED SUCCESSFULLY
        print("Taxi " + str(bookedTaxi.id) + " booked")

    def createTaxis(self):
        for i in range(4):
            t = Taxi()
            Booking.taxis.append(t)

######################################

    def main(self):

        self.createTaxis()
        while(True):
                
            print("0 - > Book Taxi")
            print("1 - > Print Taxi details")
            try:
                choice = int(input())
                
                if choice == 0:
                    customerID = 1
                    # print()
                    pickupPoint = int(input("Enter Pickup point"))
                    print("Enter Drop point")
                    dropPoint = int(input())
                    print("Enter Pickup time")
                    pickupTime = int(input())

                    if(pickupPoint < 1 or dropPoint > 6 or pickupPoint > 6 or dropPoint < 1):
                        print("Valid pickup and drop are 1,2,3,4,5,6.... Exitting.....")
                    
                    freeTaxis = self.getFreeTaxis(Booking.taxis,pickupTime,pickupPoint)

                    if(freeTaxis.__len__() == 0):
                        print("No Taxi can be alloted. Exitting")
                        continue

                    freeTaxis.sort(key=lambda x:x.totalEarnings)

                    self.bookTaxi(customerID,pickupPoint,dropPoint,pickupTime,freeTaxis)
                    customerID+=1
                    continue
                    
                else:
                    # //two functions to print details
                    
                    # for t in Booking.taxis:
                    #     t.printTaxiDetails()
                    for t in Booking.taxis:
                        t.printDetails()
                    continue
            except ValueError:
                continue

q = Booking()
q.main()