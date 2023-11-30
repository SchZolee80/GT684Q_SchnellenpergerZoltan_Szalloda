# Szoba osztály létrehozása
class Szoba:
    def __init__(self, szobaszam, ar):
        self._szobaszam = szobaszam
        self._ar = ar

    @property
    def szobaszam(self):
        return self._szobaszam

    @property
    def ar(self):
        return self._ar

    @property
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
        self._nev = nev
        self._szobak = []
        self._foglalasok = {}

    @property
    def nev(self):
        return self._nev

    @property
    def szobak(self):
        return self._szobak

    @property
    def foglalasok(self):
        return self._foglalasok

    def add_szoba(self, szoba):
        self._szobak.append(szoba)

    def listaz_szobak(self):
        for szoba in self._szobak:
            print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar}")

    def foglalas(self, szoba, datum):
        if szoba not in self.foglalasok:
            self._foglalasok[szoba] = {}

        if datum not in self.foglalasok[szoba]:
            self._foglalasok[szoba][datum] = True
            return szoba.ar
        else:
            print(f"A szoba már foglalt ezen a dátumon.")
            return None

    def lemondas(self, szoba, datum):
        if szoba in self.foglalasok and datum in self.foglalasok[szoba]:
            del self._foglalasok[szoba][datum]
            print(f"Foglalás lemondva a(z) {datum} dátumon.")
        else:
            print(f"A megadott foglalás nem található.")

    def listaz_foglalasok(self):
        print("A Hotel foglalásai:")
        for szoba, foglalasok in self._foglalasok.items():
            for datum in foglalasok.keys():
                print(f"Szobaszám: {szoba.szobaszam}, Dátum: {datum}")

    def listaz_elerheto_szobak(self):
        print(f"A {self.nev} szálloda elérhető szobái:")
        for szoba in self.szobak:
            print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar}, Típus: {szoba.get_szoba_tipus()}")


# Foglalás osztály létrehozása
class Foglalas:
    def __init__(self, szoba, datum):
        self._szoba = szoba
        self._datum = datum

    @property
    def szoba(self):
        return self._szoba

    @property
    def datum(self):
        return self._datum


def felhasznaloi_interface():
    while True:
        print("\nVálasszon műveletet:")
        print("0. Szobák listázása")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        choice = input("Adja meg a választott művelet számát: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Hibás bemenet. Kérem, adjon meg egy számot.")
            continue

        if choice == 0:
            print(f"Szobák listája: ")
            szalloda.listaz_szobak()
        elif choice == 1:
            szobaszam = input("Adja meg a szobaszámot: ")
            datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            szoba = find_szoba(szalloda, szobaszam)
            if szoba:
                ertek = szalloda.foglalas(szoba, datum)
                if ertek is not None:
                    print(f"Foglalás sikeres. Fizetendő összeg: {ertek}")
            else:
                print(f"A megadott szobaszám nem található.")
        elif choice == 2:
            szobaszam = input("Adja meg a szobaszámot: ")
            datum = input("Adja meg a lemondás dátumát (ÉÉÉÉ-HH-NN): ")
            szoba = find_szoba(szalloda, szobaszam)
            if szoba:
                szalloda.lemondas(szoba, datum)
            else:
                print(f"A megadott szobaszám nem található.")
        elif choice == 3:
            szalloda.listaz_foglalasok()
        elif choice == 4:
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás. Kérem, válasszon újra.")


def find_szoba(szalloda, szobaszam):
    for szoba in szalloda.szobak:
        if szoba.szobaszam == szobaszam:
            return szoba
    return None


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
szalloda.add_szoba(ketagyas_szoba2)
szalloda.add_szoba(ketagyas_szoba3)
szalloda.add_szoba(ketagyas_szoba4)
print(szalloda.nev)

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

# Felhasználói interface teszt
felhasznaloi_interface()
