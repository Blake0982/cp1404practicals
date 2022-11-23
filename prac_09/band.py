"""

"""


class Band:
    """ Band Class is a group of musicians  """

    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return str(self.dispay_band())

    def dispay_band(self):
        print(f"{self.name} ({[member for member in self.members]})")
        for member in self.members:
            print(f"{member.play()}")

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a musician to the Band."""
        self.members.append(member)
