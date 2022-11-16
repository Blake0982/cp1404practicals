"""
Guitar class
will create a class for a guitar that store the values:
name, year and cost
Time: 15mins
"""
CURRENT_YEAR = 2022


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ The string that will occur if the Guitar object is called"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"


    def get_age(self):
        """gets the age of the guitar to be used by the is_vintage function"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """ determines if the guitar is older than 50 if so it is 'vintage' """
        age = self.get_age()
        if age > 50:
            return True

        return False

    def __lt__(self, other):
        return self.year < other.year
