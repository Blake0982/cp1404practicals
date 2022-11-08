"""
CP1404 Prac 7 Intermediate Exercise myguitars.py
time taken:
est:
Actual:
"""
FILENAME = "guitars.csv"
from prac_06.guitar import Guitar


def main():
    infile = open(FILENAME, 'r')
    for line in infile:
        parts = line.strip().split(',')
        print(parts)
        guitars = Guitar(parts[0], int(parts[1]), float(parts[2]))
        print(guitars)


main()
