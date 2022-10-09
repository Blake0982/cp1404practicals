MAXIMUM = 45
MINIMUM = 1
NUMBER_PER_LINE = 6
import random

number_of_quick_picks = int(input("How many quick picks? "))
from random import randint
for i in range(0, number_of_quick_picks, 1):
    random_numbers = []
    for n in range(0, NUMBER_PER_LINE, 1):
        random_numbers = random_numbers + [random.randint(MINIMUM, MAXIMUM)]
        random_numbers.sort()
    print(" ".join(f"{number:2}" for number in random_numbers))
