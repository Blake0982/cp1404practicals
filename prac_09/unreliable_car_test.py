"""
conducts two test objects one on the high reliability and one on the low reliability
"""
from unreliable_car import UnreliableCar


def main():
    test_reliably_car()
    test_unreliable_car()


def test_unreliable_car():
    my_unreliable_car = UnreliableCar(100, "Holden Cruz", 20)
    print(my_unreliable_car)
    my_unreliable_car.drive(40)
    print(my_unreliable_car)


def test_reliably_car():
    my_reliable_car = UnreliableCar(100, "Prius 1", 99)
    print(my_reliable_car)
    my_reliable_car.drive(40)
    print(my_reliable_car)


main()
