from location import Location
from vehicle import Vehicle
from ride_sharing_service import RideSharingServiceApp
from driver import Driver
from passenger import Passenger

loc1=Location(15.3243,81.2312)
loc2=Location(16.6541,82.8242)
loc3=Location(15.9812,82.8483)

car=Vehicle("CS9999","Car")
bike=Vehicle("PQ4211","Bike")

driver1=Driver("Alice",loc2,car)
driver2=Driver("Bob",loc3,bike)

Passenger1=Passenger("Anirudh",loc1)
Passenger2=Passenger("Vandana",loc2)

ride_sharing_service=RideSharingServiceApp()
ride_sharing_service.add_driver(driver1)
ride_sharing_service.add_driver(driver2)
ride_sharing_service.add_passenger(Passenger1)
ride_sharing_service.add_passenger(Passenger2)

ride_sharing_service.bookRide(Passenger1,30)
ride_sharing_service.bookRide(Passenger2,50)
ride_sharing_service.bookRide(Passenger2,30)

