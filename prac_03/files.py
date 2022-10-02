"""
1
"""
name = input("Name?")
OUTPUT_FILE = f"{name}.txt"
out_file = open(OUTPUT_FILE, 'w')
print(f"{name}", file=out_file)
out_file.close()
"""
2
"""
in_file = open(OUTPUT_FILE, 'r')
file_contents = in_file.read()
print(file_contents)
out_file.close()
"""
3
"""
total = 0
in_file = open("numbers.txt", 'r')
for i in range(0, 2, 1):
    numbers = int(in_file.readline())
    total = numbers + total
print(total)
in_file.close()
"""
4
"""
total = 0
in_file = open("numbers.txt", 'r')
lines = in_file.readlines()
number_of_lines = len(lines)
in_file.close()
in_file = open("numbers.txt", 'r')
for i in range(0, number_of_lines, 1):
    number = int(in_file.readline())
    total = number + total
print(total)
in_file.close()
