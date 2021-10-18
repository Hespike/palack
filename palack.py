class Palack(object):
    def __init__(self, ital = 1, max_urtartalom = 1, _jelenlegi_urtartalom = 1):
        self.ital = ital
        self.max_urtartalom = max_urtartalom
        self._jelenlegi_urtartalom = _jelenlegi_urtartalom

    @property
    def jelenlegi_urtartalom(self):
        return self._jelenlegi_urtartalom

    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, ertek):
        if ertek > self.max_urtartalom:
           self._jelenlegi_urtartalom = self.max_urtartalom
        elif ertek == 0:
           self.ital = None
        else:
           self._jelenlegi_urtartalom = ertek

    def suly(self, max_urtartalom, _jelenlegi_urtartalom):
        suly = max_urtartalom / 35 + self._jelenlegi_urtartalom
        return suly

    def __str__(self):
        return "Palack, benne levo ital: " + self.ital + ", jelenleg " + str(self._jelenlegi_urtartalom) + " ml van benne, maximum " + str(self.max_urtartalom) + " ml fer bele."

    def __eq__(self, palack2):
        if type(self) == type(palack2):
            return str(self.ital) == str(palack2.ital) and str(self.max_urtartalom) == str(palack2.max_urtartalom) and str(self.jelenlegi_urtartalom) == str(palack2.jelenlegi_urtartalom)
        else:
            return False

    def __iadd__(self, palack2):
        if (type(self) == type(palack2)):
            osszeg = palack2.jelenlegi_urtartalom + self._jelenlegi_urtartalom
            if (self.ital == palack2.ital):
                self.ital = self.ital
                self.jelenlegi_urtartalom = osszeg
                return self
            elif (self._jelenlegi_urtartalom == 0 or self.ital == None):
                self.ital = palack2.ital
                self.jelenlegi_urtartalom = osszeg
                return self
            else:
                self.ital = "keverek"
                self.jelenlegi_urtartalom = osszeg
                return self
        else:
            return self

class VisszavalthatoPalack(Palack):
    def __init__(self, ital, max_urtartalom = 1, jelenlegi_urtartalom = 1, palackdij = 25):
        super().__init__(ital,max_urtartalom,jelenlegi_urtartalom)
        self.palackdij = palackdij
    def __str__(self):
        return "VisszavalthatoPalack, benne levo ital: " + self.ital + ", jelenleg " + str(self.jelenlegi_urtartalom) + " ml van benne, maximum " + str(self.max_urtartalom) + " ml fer bele."

class Rekesz(object):
    def __init__(self, max_teherbiras):
        self.max_teherbiras = max_teherbiras
        self.palackok = list()

    def suly(self):
        sum = 0
        if len(self.palackok) == 0:
            return 0
        for i in range(0, len(self.palackok)):
            sum += self.palackok[i].suly()
        return sum

    def uj_palack(self, param):
        if isinstance(param, Palack):
            var = self.suly() + param.suly()
            if var < self.max_teherbiras:
                self.palackok.append(param)

    def osszes_penz(self):
        penz = 0
        for i in range(0, len(self.palackok)):
            if isinstance(self.palackok[i], VisszavalthatoPalack):
                penz += self.palackok[i].palackdij
        return penz
