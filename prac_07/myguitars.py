"""
CP1404 Prac 7 Intermediate Exercise myguitars.py
time taken:
est:20min
Actual:25min
this was added to the guitars class from prac 6
    def __lt__(self, other):
        return self.year < other.year
"""
from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    read_guitars_from_file(guitars)
    get_users_guitars(guitars)
    outfile = open(FILENAME, 'w')
    for guitar in guitars:
        print(f"{guitar[0]},{guitar[1]},{guitar[2]}", file=outfile)
    outfile.close()

def read_guitars_from_file(guitars):
    """uses the csv file """
    infile = open(FILENAME, 'r')

    for line in infile:
        parts = line.strip().split(',')
        print(parts)
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        print(guitar)
        guitars.append(guitar)
    guitars.sort()
    print(guitars[0], guitars[1], guitars[2])
    infile.close()


def get_users_guitars(guitars):
    """ this function gets the guitars and the details from the user"""
    name_of_guitar = str(input("Name:"))
    while name_of_guitar != "":
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        print(f"{name_of_guitar}({year}): ${cost:.2f}")
        guitars.append(Guitar(name_of_guitar, year, cost))
        name_of_guitar = str(input("Name:"))



main()
