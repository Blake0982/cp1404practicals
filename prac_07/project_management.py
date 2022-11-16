"""
time taken:
est: 1.5hrs
actual: 2hrs
"""
from prac_07.project import Project
import datetime

FILENAME = "projects.txt"


# if no valid file name given the program will use


def main():
    """Main function connects all the functions in a central function"""
    projects = []
    display_menu()
    user_input = input(">>>").upper()
    while user_input != "Q":
        if user_input == "L":
            print("Load File")
            load_file(projects)
        elif user_input == "S":
            print("Save File")
            save_data_to_file(projects)
        elif user_input == "D":
            display_projects(projects)
        elif user_input == "F":
            print("filter")
            filter_projects(projects)
        elif user_input == "A":
            print("Add Project")
            add_project(projects)
        elif user_input == "U":
            print("Update Project")
            update_project(projects)
        else:
            print("Invalid Menu Choice")
        display_menu()
        user_input = input(">>>").upper()
    print("Thank you for using custom-built project management software.")


def display_menu():
    """Displays the menu for selection"""
    print("(L)oad projects \n"
          "(S)ave Projects\n"
          "(D)isplay projects\n"
          "(F)ilter projects by date\n"
          "(A)dd new project\n"
          "(U)pdate project\n"
          "(Q)uite")


def load_file(projects):
    """Loads the projects from chosen file, if no file
    found it will use the default file assigned at the top of the program"""
    file_name = input("File Name:\n>>>")
    try:
        infile = open(file_name, 'r')
    except FileNotFoundError:
        print(f"file not found, using the default file: {FILENAME}")
        file_name = FILENAME
        infile = open(file_name, 'r')
    infile.readline()
    for line in infile:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    infile.close()
    print(f"Data loaded from {file_name}")


def save_data_to_file(projects):
    """Saves the updated projects and new projects to the designated file"""
    file_name = input("File Name:\n>>>")
    outfile = open(file_name, 'w')
    print(f"Name\tStart Data\tPriority\t"
          f"Cost Estimate\tCompletion Percentage", file=outfile)
    for project in projects:
        print(f"{project.name}\t{project.start_data}\t{project.priority}\t"
              f"{project.cost_estimate}\t{project.completion_percentage}", file=outfile)
    outfile.close()
    print(f"Data saved to {file_name}")


def display_projects(projects):
    """Will Display the projects from the file and added from the
    add function sorted by priority and competed or not"""
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    complete_projects.sort()
    incomplete_projects.sort()
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(project)
    print("Compete Projects:")
    for project in complete_projects:
        print(project)


def filter_projects(projects):
    """Uses date time module to filter projects by data"""
    is_finished = False
    while not is_finished:
        try:
            filter_date_string = input("Show Projects that start after date (dd/mm/yyyy): ")
            filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
            is_finished = True
        except ValueError:
            print("Invalid date try again")
    for project in projects:
        date_string = project.start_data
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        if date >= filter_date:  # error in variable might not be assigned
            print(project)


def add_project(projects):
    """Adds new project using the 'Project' class"""
    print("Let's add a new project")
    name = input("Name: ")
    is_finished = True
    while is_finished:
        try:
            start_date_string = input("Start Date (dd/mm/yyyy): ")
            start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
            is_finished = False
        except ValueError:
            print("Invalid Date (dd/mm/yyyy)")
    while not is_finished:
        try:
            priority = int(input("Priority: "))
            is_finished = True
        except ValueError:
            print("Invalid priority please enter a priority number")
    while is_finished:
        try:
            cost_estimate = float(input("Cost Estimate: $"))
            is_finished = False
        except ValueError:
            print("Invalid cost, please enter valid cost number")
    while not is_finished:
        try:
            completion_percentage = int(input("Percent Compete: "))
            if completion_percentage > 100:
                print("invalid percentage, can not be >100%")
            else:
                is_finished = True
        except ValueError:
            print("Invalid percentage, please enter valid percentage")
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print(project)
    print("Project Added")


def update_project(projects):
    """Updates the projects completion and priority"""
    for i, project in enumerate(projects):
        print(i, project)
        project_count = i
    is_finished = False
    while not is_finished:
        try:
            project_choice = int(input("Project Choice:"))
            if project_choice > project_count:
                print("invalid choice, no project found")
            else:
                is_finished = True
        except ValueError:
            print("invalid number, Please enter number")
    for i, project in enumerate(projects):
        if project_choice == i:
            print(project)
            project.completion_percentage = int(input("New Percentage:"))
            project.priority = int(input("New Priority:"))
            print(f"{project.name} has been updated")


main()
