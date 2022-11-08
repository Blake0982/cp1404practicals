"""

"""
from project import Project

FILENAME = "projects.txt"


def main():
    print("(L)oad projects \n"
          "(S)ave Projects\n"
          "(D)isplay projects\n"
          "(F)ilter projects by date\n"
          "(A)dd new project\n"
          "(U)pdate project\n"
          "(Q)uite")
    user_input = input(">>>").upper()
    while user_input != "Q":
        if user_input == "L":
            print("load")
        elif user_input == "S":
            print("SAVE")
        elif user_input == "D":
            print("Display")
        elif user_input == "F":
            print("filter")
        elif user_input == "A":
            print("add")
        elif user_input == "U":
            print("update")
        else:
            print("Invalid Menu Choice")
        user_input = input(">>>").upper()


main()
