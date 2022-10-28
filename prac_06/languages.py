"""
start time: 10:45am
finish time:10:40
total:55 mins - 10 mins for time taken for marking previous prac
new total = 45 mins :)
"""
from prac_06.programing_language import ProgrammingLanguage


def main():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    languages = [java, python, ruby, visual_basic]
    dynamic_languages = []
    for langauge in languages:
        if langauge.is_dynamic():
            dynamic_languages += langauge.name.split()
    print("The dynamic typed languages are:")
    for langauge_name in dynamic_languages:
        print(f"{langauge_name}")


main()
