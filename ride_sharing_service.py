from typing import List
from passenger import Passenger
from driver import Driver
from location import Location
from math import sqrt
from vehicle import Vehicle
class RideSharingServiceApp:
    def __int__(self):
        self.drivers:List[Driver]=[]
        self.passengers:List[Passenger]=[]
    # Method to add a Driver
    def add_driver(self,driver:Driver):
        self.drivers.append(driver)
    def __calcDistance(self,location1:Location,location2:Location):
        # Euclidean Distanc
        dx:float=location1.get_latitute()-location2.get_latitute()
        dy:float=location1.get_longitude()-location2.get_longitude()
        return sqrt(dx*dx + dy*dy)
    
    def __calcFare(self,vehicle:Vehicle,distance:float):
        if vehicle.type=="Car":
            return distance*20
        elif vehicle.type=="Bike":
            return distance*12
        else:
            return distance*8
        
    # Method to add a passenger
    def add_passenger(self,passenger:Passenger):
        self.passengers.append(passenger)
    # Method to book ride
    def bookRide(self,passenger:Passenger,distance):
        if len(self.drivers)==0:
            print(f"No driver avaliable for {passenger.name}")
            return
        assignedDriver=None
        minDistance=float("inf")
        for driver in self.drivers:
            currentDriverDistance=self.__calcDistance(passenger.location,driver.location)
            if currentDriverDistance<minDistance:
                minDistance=currentDriverDistance
                assignedDriver=driver
            
        #fare calculate
        expectedFare:float=self.__calcFare(assignedDriver.vehicle,distance)
        
        #show the driver and fare to the passenger
        print(f"Ride booked for {passenger.name} with driver {assignedDriver.name} with fare of Rs.{expectedFare}")
        print(f"Driver is on the way and is {minDistance}km away")