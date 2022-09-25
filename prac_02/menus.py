"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
name = input("Enter name: ")


def menu_options():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uite")
    choice = input(">>> ").upper()


def menu():
    menu_options()
    while choice != "Q":
        if choice == "H":
            print("Hello", name)
        elif choice == "G":
            print("Goodbye", name)
        else:
            print("invalid choice")
        menu_options()
    print("finished")


menu()
