# Szoba osztály létrehozása
class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    def get_szoba_tipus(self):
        pass


# EgyagyasSzoba osztály létrehozása
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 20000)  # Példának megfelelő ár beállítása


# KetagyasSzoba osztály létrehozása
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 30000)  # Példának megfelelő ár beállítása


# Szalloda osztály létrehozása
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = {}

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def listaz_szobak(self):
        for szoba in self.szobak:
            print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar}, Típus: {szoba.get_szoba_tipus()}")

    def foglalas(self, szoba, datum):
        if szoba not in self.foglalasok:
            self.foglalasok[szoba] = {}

        if datum not in self.foglalasok[szoba]:
            self.foglalasok[szoba][datum] = True
            return szoba.ar
        else:
            print(f"A szoba már foglalt ezen a dátumon.")
            return None

    def lemondas(self, szoba, datum):
        if szoba in self.foglalasok and datum in self.foglalasok[szoba]:
            del self.foglalasok[szoba][datum]
            print(f"Foglalás lemondva a(z) {datum} dátumon.")
        else:
            print(f"A megadott foglalás nem található.")

    def listaz_foglalasok(self):
        print("A Hotel foglalásai:")
        for szoba, foglalasok in self.foglalasok.items():
            for datum in foglalasok.keys():
                print(f"Szobaszám: {szoba.szobaszam}, Dátum: {datum}")


# Foglalás osztály létrehozása
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


# Tesztelés
egyagyas_szoba1 = EgyagyasSzoba("111")
ketagyas_szoba1 = KetagyasSzoba("222")
ketagyas_szoba2 = KetagyasSzoba("223")
ketagyas_szoba3 = KetagyasSzoba("224")
ketagyas_szoba4 = KetagyasSzoba("225")

# Szobaszém kiír
print(egyagyas_szoba1.szobaszam)

# Szálloda létrehoz és hozzáadjuk a szobákat
szalloda = Szalloda("Varjó Hotel")
szalloda.add_szoba(egyagyas_szoba1)
szalloda.add_szoba(ketagyas_szoba1)
print(szalloda.nev)
szalloda.listaz_szobak()

# Foglalas teszt
datum = "2023-12-01"
datum2 = "2023-12-02"
szalloda.foglalas(egyagyas_szoba1, datum2)
szalloda.foglalas(ketagyas_szoba1, datum2)
szalloda.foglalas(ketagyas_szoba2, datum2)
szalloda.foglalas(egyagyas_szoba1, datum)  # Rá lehet foglalni
foglalas_osszeg = szalloda.foglalas(egyagyas_szoba1, datum)


if foglalas_osszeg is not None:
    print(f"Foglalás sikeres. Fizetendő összeg: {foglalas_osszeg}")

# Lemondás teszt
szalloda.lemondas(egyagyas_szoba1, datum2)

# Foglalás Listázás
szalloda.listaz_foglalasok()
