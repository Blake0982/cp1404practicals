def number_part():
    numbers = []
    for i in range(0, 5, 1):
        numbers = numbers + [int(input("Number: "))]
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest nuber is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average}")


number_part()


def username_part():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_input = input("username:")
    if user_input in usernames:
        print("Access Granted")
    else:
        print("Access denied")


username_part()