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
    guitars.sort()
    outfile = open(FILENAME, 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=outfile)
    outfile.close()


def read_guitars_from_file(guitars):
    """uses the csv file """
    infile = open(FILENAME, 'r')
    for line in infile:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    infile.close()


def get_users_guitars(guitars):
    """
    this function gets the guitars and the details from the user,
    this is straight out of prac 6
    """
    print("Enter New Guitars")
    name = str(input("Name:"))
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        print(f"{name}({year}): ${cost:.2f}")
        guitars.append(Guitar(name, year, cost))
        name = str(input("Name:"))


main()
