"""
Prac 5
"""


def main():
    global fullname
    email_to_name = {}
    email = input("Email:")
    while email != "":
        find_name(email)
        email_to_name[email] = fullname
        email = input("Email:")
    for email, fullname in email_to_name.items():
        print(f"{fullname} ({email})")


def find_name(email):
    global fullname
    name = email.split("@")[0]
    name = name.split(".")
    try:
        fullname = name[0] + " " + name[1]
        fullname = fullname.title()
        print(f"Is your name: {fullname}?")
    except IndexError:
        print(f"Is your name: {name}?")
    answer = input("Y/N: ").upper()
    if answer.startswith("N"):
        fullname = input("Name:")


main()
