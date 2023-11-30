from datetime import datetime

# Szoba osztály létrehozása


class Szoba:
    def __init__(self, szobaszam, ar):
        self._szobaszam = szobaszam
        self._ar = ar

    def is_valid_date(self, datum):
        try:
            date_obj = datetime.strptime(datum, "%Y-%m-%d")
            return date_obj >= datetime.now()
        except ValueError:
            return False

    @property
    def szobaszam(self):
        return self._szobaszam

    @property
    def ar(self):
        return self._ar

    @ar.setter
    def ar(self, value):
        if value >= 0:
            self._ar = value
        else:
            print("Az ár nem lehet negatív.")

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

    def is_room_available(self, szoba, datum):
        if szoba in self._foglalasok and datum in self._foglalasok[szoba]:
            return False
        return True

    def foglalas(self, szoba, datum):
        if not szoba.is_valid_date(datum):
            print("Érvénytelen dátum. Kérem, adjon meg egy jövőbeli dátumot.")
            return None

        if not self.is_room_available(szoba, datum):
            print(f"A szoba már foglalt ezen a dátumon.")
            return None

        if szoba not in self._foglalasok:
            self._foglalasok[szoba] = {}

        self._foglalasok[szoba][datum] = True
        return szoba.ar

    def kezdeti_betoltes(self):
        egyagyas_szoba1 = EgyagyasSzoba("111")
        ketagyas_szoba1 = KetagyasSzoba("222")
        ketagyas_szoba2 = KetagyasSzoba("223")
        ketagyas_szoba3 = KetagyasSzoba("224")
        ketagyas_szoba4 = KetagyasSzoba("225")

        self.add_szoba(egyagyas_szoba1)
        self.add_szoba(ketagyas_szoba1)
        self.add_szoba(ketagyas_szoba2)
        self.add_szoba(ketagyas_szoba3)
        self.add_szoba(ketagyas_szoba4)

        datum = "2023-12-31"
        datum1 = "2023-12-01"
        datum2 = "2023-12-02"
        self.foglalas(egyagyas_szoba1, datum2)
        self.foglalas(ketagyas_szoba1, datum2)
        self.foglalas(ketagyas_szoba2, datum2)
        self.foglalas(ketagyas_szoba3, datum1)
        self.foglalas(ketagyas_szoba4, datum)
        self.foglalas(egyagyas_szoba1, datum)  # Rá lehet foglalni

    def lemondas(self, szoba, datum):
        if szoba in self._foglalasok and datum in self._foglalasok[szoba]:
            del self._foglalasok[szoba][datum]
            print(f"Foglalás lemondva a(z) {datum} dátumon.")
        else:
            print(f"A megadott foglalás nem található. Lemondás sikertelen.")

    def listaz_foglalasok(self):
        print("A Hotel foglalásai:")
        for szoba, foglalasok in self._foglalasok.items():
            for datum in foglalasok.keys():
                print(f"Szobaszám: {szoba.szobaszam}, Dátum: {datum}")

    def listaz_elerheto_szobak(self):
        print(f"A {self.nev} szálloda elérhető szobái:")
        for szoba in self.szobak:
            print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar}")

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


def felhasznaloi_interface(szalloda):
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


szalloda = Szalloda("Varjó Hotel")
szalloda.kezdeti_betoltes()
felhasznaloi_interface(szalloda)
