"""
code used for testing the guitar class
time taken for class creation: 10 mins
time taken for test program: 10 mins
"""
from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar)

if guitar.is_vintage():
    print(f"{guitar.name} is vintage")
print(guitar.get_age())
