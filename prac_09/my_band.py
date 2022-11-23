"""Band example with list of musicians."""
from band import Band
from musician import Musician
from guitar import Guitar


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
