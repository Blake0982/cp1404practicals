"""
CP1404 Prac 7 Intermediate Exercise myguitars.py
time taken:
est:
Actual:
"""
from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    infile = open(FILENAME, 'r')
    guitars = []
    for line in infile:
        parts = line.strip().split(',')
        print(parts)
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        print(guitar)
        guitars.append(guitar)
    guitars.sort()
    print(guitars[0], guitars[1],guitars[2])
    infile.close()


main()
