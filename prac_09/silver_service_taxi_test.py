from silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi(100, "Prius 1", 3)
    print(my_taxi)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, Current fare: ${my_taxi.get_fare()}")


main()