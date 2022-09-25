def get_score():
    print("Enter a valid score from 0 to 100")
    global score
    score = int(input("Enter score: "))


def main():
    if score < 50:
        print("Bad")
    elif score >= 90:
        print("Excellent")
    else:
        print("Passable")


def print_stars():
    print('*' * score)


def menu_options():
    global choice
    print("(E)nter Score")
    print("(Q)uite")
    choice = input(">>> ").upper()


def menu():
    global choice
    while choice != "Q":
        if choice == "E":
            get_score()
            if score > 100 or score < 0:
                print("Invalid score")
            else:
                main()
                print_stars()
        else:
            print("invalid choice")
        print("(E)nter Score")
        print("(Q)uite")
        choice = input(">>> ").upper()
    print("finished ")


menu_options()

menu()
