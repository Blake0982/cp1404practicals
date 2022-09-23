password = input("Password:")
password_length = len(password)
while password_length < 10:
    print('*' * password_length)
    print("invalid password length, must be at least 10 letters")
    password = input("Password:")
    password_length = len(password)
print('*' * password_length)
print("valid password length")
