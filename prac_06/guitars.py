"""

"""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    get_guitars(guitars)
    sample_guitars(guitars)
    print(f"... snip ...\n \nThese are my guitars:")
    show_guitars(guitars)


def sample_guitars(guitars):
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


def get_guitars(guitars):
    name_of_guitar = str(input("Name:"))
    while name_of_guitar != "":
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        print(f"{name_of_guitar}({year}): ${cost:.2f}")
        guitars.append(Guitar(name_of_guitar, year, cost))
        name_of_guitar = str(input("Name:"))


def show_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
