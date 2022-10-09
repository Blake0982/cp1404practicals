"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    get_data()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data = subject_data + [parts]
    input_file.close()
    print_data(line, subject_data)


def print_data(line, subject_data):
    for i in range(0, 3, 1):
        data = subject_data[i]
        subject = line.split(',')
        subject = data[0]
        lecture = data[1]
        number_of_students = data[2]
        print(f"{subject} is taught by {lecture} and has {number_of_students} students")


main()
