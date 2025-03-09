class Homoniewiadomo:
    def __init__(self, nazwa, wiek, umiejętność):
        self.czy_zyje = True
        self.nazwa = nazwa
        self.wiek = wiek
        self.umiejętność = umiejętność

    def czy_zyje_inf(self):
        return self.czy_zyje

class Dzikus_z_Afryki(Homoniewiadomo):
    def __init__(self, nazwa, wiek, umiejętność):
        super().__init__(nazwa, wiek, umiejętność)

    def belkot(self):
        print("prosze daj wody")

class Afroamerykanin(Dzikus_z_Afryki):
    def __init__(self, nazwa, wiek, umiejętność, praca):
        super().__init__(nazwa, wiek, umiejętność)
        self.praca = praca

    def czarno_to_widze(self):
        print(f"JOŁ JOŁ NIG...!!!")

class Amerykanin(Afroamerykanin):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu):
        super().__init__(nazwa, wiek, umiejętność, praca)
        self.procent_tłuszczu = procent_tłuszczu

    def amerykanin_do_afroamerykanina(self):
        print("Twoj dziadek kiedyś był moim niewolnikiem")

class Brytyjczyk_z_rodziny_kolonistów(Amerykanin):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu)
        self.ilość_wypitych_herbat = ilość_wypitych_herbat

    def yapping(self):
        print("Elizabeth zaparz herabatę.")

class Ojciec_brytyjczyka(Brytyjczyk_z_rodziny_kolonistów):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat)
        self.dzieci = dzieci

    def kolonia(self):
        print("tutaj będzie farma trzciny cukrowej")

class dziadek_afroamerykańca(Ojciec_brytyjczyka):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci)
        self.godziny_w_pracy = godziny_w_pracy

    def farma_trzciny(self):
        print("nasram im do trzciny hehe")

class Założyciel_farmy(dziadek_afroamerykańca):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy)
        self.ilość_niewolników = ilość_niewolników

    def usłyszał_afroamerykańca(self):
        print("za takie pomysły dostaniesz 10 razy tym batem")

class Kuzyn_założyciela(Założyciel_farmy):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników)
        self.rodzeństwo = rodzeństwo

    def ciekaw_świata_za_oceanem(self):
        print("napiszę list do kuzyna jak tam idzie uprawa trzciny")

class Przyjaciel_kuzyna(Kuzyn_założyciela):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo)
        self.hobby = hobby

    def polowanie(self):
        print("polujemy na dzikie zwierzęta")

class Siostra_przyjaciela(Przyjaciel_kuzyna):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby)
        self.ulubione_potrawy = ulubione_potrawy

    def gotowanie(self):
        print("gotuje dla całej rodziny")

class Matka_siostry(Siostra_przyjaciela):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy)
        self.doświadczenie = doświadczenie

    def nauczanie(self):
        print("uczy dzieci jak gotować")

class Babcia_matki(Matka_siostry):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści)
        self.opowieści = opowieści

    def opowiadanie(self):
        print("opowiada o swoich czasach")

class Dziadek_babci(Babcia_matki):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści)
        self.wojenne_doświadczenia = wojenne_doświadczenia

    def wojenne_opowieści(self):
        print("opowiada o swoich wojennych przygodach")

class Przyjaciel_dziadka(Dziadek_babci):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia)
        self.wspólne_wspomnienia = wspólne_wspomnienia

    def wspomnienia(self):
        print("wspomina o wspólnych czasach")

class Siostra_przyjaciela(Przyjaciel_dziadka):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia)
        self.ulubione_muzyka = ulubione_muzyka

    def muzyka(self):
        print("słucha swojej ulubionej muzyki")

class Matka_siostry_przyjaciela(Siostra_przyjaciela):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka)
        self.umiejętności_domowe = umiejętności_domowe

    def domowe_obowiązki(self):
        print("wykonuje domowe obowiązki")

class Babcia_matki_siostry_przyjaciela(Matka_siostry_przyjaciela):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe)
        self.tradycje = tradycje

    def tradycyjne_święta(self):
        print("celebruje tradycyjne święta")

class Dziadek_babci_matki_siostry(Babcia_matki_siostry_przyjaciela):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje)
        self.historia_rodziny = historia_rodziny

    def opowieść_o_rodzinie(self):
        print("opowiada o swojej historii rodzinnych doświadczeń")

class Przyjaciel_dziadka_babci_matki_siostry(Dziadek_babci_matki_siostry):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania)
        self.wspólne_zainteresowania = wspólne_zainteresowania

    def wspólne_zajęcia(self):
        print("spędza czas na wspólnych zajęciach")

class Siostra_przyjaciela_dziadka_babci_matki_siostry(Przyjaciel_dziadka_babci_matki_siostry):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy)
        self.ulubione_filmy = ulubione_filmy

    def filmy(self):
        print("ogląda swoje ulubione filmy")

class Matka_siostry_przyjaciela_dziadka_babci_matki_siostry(Siostra_przyjaciela_dziadka_babci_matki_siostry):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy)
        self.umiejętności_kulinarnie = umiejętności_kulinarnie

    def gotowanie_dla_rodziny(self):
        print("gotuje dla swojej rodziny")

class Babcia_matki_siostry_przyjaciela_dziadka_babci_matki_siostry(Matka_siostry_przyjaciela_dziadka_babci_matki_siostry):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie, doświadczenie_kulinarnie):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie, doświadczenie_kulinarnie)
        self.doświadczenie_kulinarnie = doświadczenie_kulinarnie

    def kulinarnie_wspomnienia(self):
        print("wspomina o swoich kulinarnych doświadczeniach")

class Dziadek_babci_matki_siostry_przyjaciela_babci_matki_siostry(Babcia_matki_siostry_przyjaciela_dziadka_babci_matki_siostry):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie, doświadczenie_kulinarnie, historia_kulinarna):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie, doświadczenie_kulinarnie, historia_kulinarna)
        self.historia_kulinarna = historia_kulinarna

    def historia_kulinarna(self):
        print("opowiada o swojej historii kulinarnych doświadczeń")

class Przyjaciel_dziadka_babci_matki_siostry_babci_matki_siostry(Dziadek_babci_matki_siostry_przyjaciela_babci_matki_siostry):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie, doświadczenie_kulinarnie, historia_kulinarna, wspólne_wspomnienia_o_kuchni):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie, doświadczenie_kulinarnie, historia_kulinarna, wspólne_wspomnienia_o_kuchni)
        self.wspólne_wspomnienia_o_kuchni = wspólne_wspomnienia_o_kuchni

    def wspomnienia_o_kuchni(self):
        print("wspomina o wspólnych wspomnieniach związanych z kuchnią")

class Siostra_przyjaciela_dziadka_babci_matki_siostry_babci_matki_siostry(Przyjaciel_dziadka_babci_matki_siostry_babci_matki_siostry):
    def __init__(self, nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie, doświadczenie_kulinarnie, historia_kulinarna, wspólne_wspomnienia_o_kuchni, ulubione_książki):
        super().__init__(nazwa, wiek, umiejętność, praca, procent_tłuszczu, ilość_wypitych_herbat, dzieci, godziny_w_pracy, ilość_niewolników, rodzeństwo, hobby, ulubione_potrawy, doświadczenie, opowieści, wojenne_doświadczenia, wspólne_wspomnienia, ulubione_muzyka, umiejętności_domowe, tradycje, historia_rodziny, wspólne_zainteresowania, ulubione_filmy, umiejętności_kulinarnie, doświadczenie_kulinarnie, historia_kulinarna, wspólne_wspomnienia_o_kuchni)
        self.ulubione_książki = ulubione_książki

    def czytanie(self):
        print("czyta swoje ulubione książki")

A = Dzikus_z_Afryki("KLKIKLAKMAKALELE", 28, "łapać dzikie zwierzęta")
B = Afroamerykanin("JAMAL", 33, "strzelanie do białych", "kradzież uliczna")
C = Amerykanin("JONY", 21, "strzelanie do czaarnych", "policjant", 80)
D = Brytyjczyk_z_rodziny_kolonistów("JASON", 45, "PODBIJANIE I KOLONIZACJA", "KOLONIZACJA", 15, 999999)
E = Ojciec_brytyjczyka("JEREMY", 55, "")