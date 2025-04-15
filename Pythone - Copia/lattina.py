import math
class SodaCan :
    def __init__(self, altezza, raggio):
        self._altezza = altezza
        self._raggio = raggio
    def setGetSurfaceArea(self) :
        circonferenza = 2 * math.pi * self._raggio
        laterale = self._altezza * circonferenza
        area_base = math.pi * self._raggio ** 2
        return laterale + 2 * area_base
    def setGetVolume(self) :
        area_base = math.pi * self._raggio ** 2
        return self._altezza * area_base
   

mini_lattina = SodaCan(8, 2)
lattina = SodaCan(9.24, 3.37)

print(mini_lattina.setGetSurfaceArea())
print(lattina.setGetSurfaceArea())
print(mini_lattina.GetVolume())
print(lattina.GetVolume())

