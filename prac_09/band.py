"""

"""


class Band:
    """ Band Class is a group of musicians  """

    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({[member for member in self.members]})" \
               f"\n{[member.play() for member in self.members]}"

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a musician to the Band."""
        self.members.append(member)


if __name__ == '__main__':
    from guitar import Guitar
    from musician import Musician

    band = Band()
    assert not band.name
    assert not band.members

    band = Band('Extreme')
    nuno = Musician("Nuno Bettencourt")
    nuno.instruments.append(Guitar("Washburn N4", 1990, 2499.95))
    band.add(nuno)
    gary = Musician("Gary Cherone")
    band.add(gary)
    pat = Musician("Pat Badger")
    pat.instruments.append(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))
    band.add(pat)
    kevin = Musician("Kevin Figueiro")
    band.add(kevin)
    print(band)
