def main():
    password_length = get_password()
    while password_length < 10:
        print_stars(password_length)
        print("invalid password length, must be at least 10 letters")
        password_length = get_password()
    print_stars(password_length)
    print("valid password length")


def print_stars(password_length):
    print('*' * password_length)


def get_password():
    password = input("Password:")
    password_length = len(password)
    return password_length


main()
