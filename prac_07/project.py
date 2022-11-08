"""
Project class
"""


class Project:

    def __int__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_data = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """the string returned if the object is printed"""
        return f"Project:{self.name}, Start Date:{self.start_data}, Priority{self.priority}," \
               f"Cost Estimate:{self.cost_estimate}, {self.completion_percentage}% complete "

    def __lt__(self, other):
        return self.priority < other.priority

