"""
est: 10 mins
actual: 11 mins
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """

    """
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0
        self.flagfall += 4.50

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare_cost = super().get_fare()
        return fare_cost + self.flagfall

    def __str__(self):
        return f"{super().__str__()},Plus a Flag fall of {self.flagfall:.2f}"

