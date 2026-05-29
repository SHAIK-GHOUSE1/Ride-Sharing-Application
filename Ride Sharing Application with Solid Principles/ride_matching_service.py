from typing import List
from driver import Driver
from passenger import Passenger
from location import Location
from fare_strategy import FareStrategy
from ride import Ride,RideStatus


class RideMatchingService:
    def __init__(self):
        self.__avaliabledrivers: List[Driver] = []

    def add_driver(self, driver: Driver):
        self.__avaliabledrivers.append(driver)

    def requestRide(
        self, passenger: Passenger, distance: float, strategy: FareStrategy
    ):
        if len(self.__avaliabledrivers) == 0:
            passenger.notify("No Drivers available")
            return
        nearestDriver: Driver = self.__findNearestDriver(passenger.get_location())
        self.__avaliabledrivers.remove(nearestDriver)
        ride: Ride = Ride(passenger, nearestDriver, distance, strategy)
        ride.calculateFare()
        passenger.notify(f"Ride scheduled with fare Rs.{ride.getRideFare()}")
        nearestDriver.notify(f"You have one new ride for Rs{ride.getRideFare()}")
        ride.updateStatus(RideStatus.ONGOING)
        #After sometime
        ride.updateStatus(RideStatus.COMPLETED)
        self.__avaliabledrivers.append(nearestDriver)
        return

    def __findNearestDriver(self, passenger_location: Location):
        assignedDriver = None
        minDistance = float("inf")
        for driver in self.__avaliabledrivers:
            dist = driver.get_location().calcDistance(passenger_location)
            if dist < minDistance:
                minDistance = dist
                assignedDriver = driver
        return assignedDriver
