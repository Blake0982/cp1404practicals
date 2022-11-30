"""

"""

from car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.
                Drive given distance if car has enough fuel
                or drive until fuel runs out return the distance actually driven.
                """
        breakdown_chance = randint(1, 100)
        if breakdown_chance >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
