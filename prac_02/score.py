"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def get_score():
    global score
    score = float(input("Enter score: "))


def main():
    if score >= 100 or score < 0:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif score >= 90:
        print("Excellent")
    else:
        print("Passable")


def get_random_number():
    global score
    from random import randint
    score = randint(0, 100)
    print("random score value", score)


get_score()

main()

get_random_number()

main()
