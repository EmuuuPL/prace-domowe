class Osoba:
    def __init__(self, imie, wiek, umiejetnosc):
        self.zyje = True
        self.imie = imie
        self.wiek = wiek
        self.umiejetnosc = umiejetnosc

    def czy_zyje(self):
        return self.zyje

    def przedstaw_sie(self):
        return f"Nazywam się {self.imie}, mam {self.wiek} lat i moją umiejętnością jest {self.umiejetnosc}"


class Pracownik(Osoba):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie):
        super().__init__(imie, wiek, umiejetnosc)
        self.zawod = zawod
        self.doswiadczenie = doswiadczenie

    def pracuj(self):
        print(f"{self.imie} pracuje jako {self.zawod}")


class Nauczyciel(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, przedmiot):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.przedmiot = przedmiot

    def ucz(self):
        print(f"{self.imie} uczy przedmiotu {self.przedmiot}")


class Artysta(Osoba):
    def __init__(self, imie, wiek, umiejetnosc, dziedzina_sztuki):
        super().__init__(imie, wiek, umiejetnosc)
        self.dziedzina_sztuki = dziedzina_sztuki

    def tworz(self):
        print(f"{self.imie} tworzy w dziedzinie {self.dziedzina_sztuki}")


class Muzyk(Artysta):
    def __init__(self, imie, wiek, umiejetnosc, dziedzina_sztuki, instrument):
        super().__init__(imie, wiek, umiejetnosc, dziedzina_sztuki)
        self.instrument = instrument

    def graj(self):
        print(f"{self.imie} gra na instrumencie {self.instrument}")


class Kucharz(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, specjalnosc):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.specjalnosc = specjalnosc

    def gotuj(self):
        print(f"{self.imie} przygotowuje danie w swojej specjalności: {self.specjalnosc}")


class Sportowiec(Osoba):
    def __init__(self, imie, wiek, umiejetnosc, dyscyplina, osiagniecia):
        super().__init__(imie, wiek, umiejetnosc)
        self.dyscyplina = dyscyplina
        self.osiagniecia = osiagniecia

    def trenuj(self):
        print(f"{self.imie} trenuje {self.dyscyplina}")


class Pisarz(Artysta):
    def __init__(self, imie, wiek, umiejetnosc, dziedzina_sztuki, gatunek):
        super().__init__(imie, wiek, umiejetnosc, dziedzina_sztuki)
        self.gatunek = gatunek

    def pisz(self):
        print(f"{self.imie} pisze w gatunku {self.gatunek}")


class Lekarz(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, specjalizacja):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.specjalizacja = specjalizacja

    def lecz(self):
        print(f"{self.imie} leczy pacjentów jako {self.specjalizacja}")


class Programista(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, jezyki_programowania):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.jezyki_programowania = jezyki_programowania

    def programuj(self):
        print(f"{self.imie} programuje w językach: {', '.join(self.jezyki_programowania)}")


class Tancerz(Artysta):
    def __init__(self, imie, wiek, umiejetnosc, dziedzina_sztuki, styl_tanca):
        super().__init__(imie, wiek, umiejetnosc, dziedzina_sztuki)
        self.styl_tanca = styl_tanca

    def tancz(self):
        print(f"{self.imie} tańczy w stylu {self.styl_tanca}")


class Fotograf(Artysta):
    def __init__(self, imie, wiek, umiejetnosc, dziedzina_sztuki, typ_fotografii):
        super().__init__(imie, wiek, umiejetnosc, dziedzina_sztuki)
        self.typ_fotografii = typ_fotografii

    def fotografuj(self):
        print(f"{self.imie} robi zdjęcia w kategorii {self.typ_fotografii}")


class Architekt(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, styl_architektury):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.styl_architektury = styl_architektury

    def projektuj(self):
        print(f"{self.imie} projektuje budynki w stylu {self.styl_architektury}")


class Mechanik(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, specjalizacja_pojazdow):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.specjalizacja_pojazdow = specjalizacja_pojazdow

    def naprawiaj(self):
        print(f"{self.imie} naprawia {self.specjalizacja_pojazdow}")


class Pilot(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, typ_samolotu):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.typ_samolotu = typ_samolotu

    def lataj(self):
        print(f"{self.imie} pilotuje {self.typ_samolotu}")


class Aktor(Artysta):
    def __init__(self, imie, wiek, umiejetnosc, dziedzina_sztuki, gatunek_aktorstwa):
        super().__init__(imie, wiek, umiejetnosc, dziedzina_sztuki)
        self.gatunek_aktorstwa = gatunek_aktorstwa

    def graj_role(self):
        print(f"{self.imie} gra w {self.gatunek_aktorstwa}")


class Policjant(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, jednostka):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.jednostka = jednostka

    def patroluj(self):
        print(f"{self.imie} patroluje jako funkcjonariusz {self.jednostka}")


class Strazak(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, specjalizacja_ratownicza):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.specjalizacja_ratownicza = specjalizacja_ratownicza

    def ratuj(self):
        print(f"{self.imie} prowadzi akcję ratowniczą w zakresie {self.specjalizacja_ratownicza}")


class Psycholog(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, podejscie_terapeutyczne):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.podejscie_terapeutyczne = podejscie_terapeutyczne

    def prowadz_terapie(self):
        print(f"{self.imie} prowadzi terapię w nurcie {self.podejscie_terapeutyczne}")


class Prawnik(Pracownik):
    def __init__(self, imie, wiek, umiejetnosc, zawod, doswiadczenie, specjalizacja_prawna):
        super().__init__(imie, wiek, umiejetnosc, zawod, doswiadczenie)
        self.specjalizacja_prawna = specjalizacja_prawna

    def reprezentuj(self):
        print(f"{self.imie} reprezentuje klientów w sprawach {self.specjalizacja_prawna}")

if __name__ == "__main__":
    programista = Programista("Adam", 30, "kodowanie", "programista", 5, ["Python", "Java", "JavaScript"])
    tancerz = Tancerz("Maja", 22, "taniec", "taniec współczesny", "breakdance")
    fotograf = Fotograf("Karol", 35, "fotografia", "fotografia artystyczna", "portret")
    architekt = Architekt("Zofia", 40, "projektowanie", "architekt", 15, "modernizm")
    mechanik = Mechanik("Robert", 45, "naprawa", "mechanik", 20, "samochody sportowe")
    pilot = Pilot("Michał", 38, "pilotaż", "pilot", 12, "Boeing 737")
    aktor = Aktor("Julia", 28, "aktorstwo", "teatr", "dramat")
    policjant = Policjant("Tomasz", 33, "śledztwo", "policjant", 8, "wydział kryminalny")
    strazak = Strazak("Marek", 35, "ratownictwo", "strażak", 10, "ratownictwo wysokościowe")
    psycholog = Psycholog("Anna", 40, "terapia", "psycholog", 15, "psychodynamiczne")
    prawnik = Prawnik("Piotr", 45, "prawo", "prawnik", 20, "prawo karne")


    programista.przedstaw_sie()
    programista.programuj()

    tancerz.przedstaw_sie()
    tancerz.tancz()

    fotograf.przedstaw_sie()
    fotograf.fotografuj()

    architekt.przedstaw_sie()
    architekt.projektuj()

    mechanik.przedstaw_sie()
    mechanik.naprawiaj()

    pilot.przedstaw_sie()
    pilot.lataj()

    aktor.przedstaw_sie()
    aktor.graj_role()

    policjant.przedstaw_sie()
    policjant.patroluj()

    strazak.przedstaw_sie()
    strazak.ratuj()

    psycholog.przedstaw_sie()
    psycholog.prowadz_terapie()

    prawnik.przedstaw_sie()
    prawnik.reprezentuj()