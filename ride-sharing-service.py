from typing import List
from passenger import Passenger
from driver import Driver
class RideSharingServiceApp:
    def __int__(self):
        self.drivers:List[Driver]=[]
        self.passengers:List[Passenger]=[]
    # Method to add a Driver
    def add_driver(self,driver:Driver):
        self.drivers.append(driver)
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
            currentDriverDistance=calcDistance(_____,______)
            if minDistance
            
        