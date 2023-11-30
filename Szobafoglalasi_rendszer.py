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
        super().__init__(szobaszam, 10000)  # Példának megfelelő ár beállítása


# KetagyasSzoba osztály létrehozása
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)  # Példának megfelelő ár beállítása


# Szalloda osztály létrehozása
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def listaz_szobak(self):
        for szoba in self.szobak:
            print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar}, Típus: {szoba.get_szoba_tipus()}")


# Foglalás osztály létrehozása
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum
