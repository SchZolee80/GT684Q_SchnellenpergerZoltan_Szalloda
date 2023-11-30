# Szoba osztály létrehozása
class Szoba:
    def __init__(self, szobaszam, ar):
        pass

    def get_szoba_tipus(self):
        pass

# EgyagyasSzoba osztály létrehozása
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        pass

# KetagyasSzoba osztály létrehozása
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        pass

# Szalloda osztály létrehozása
class Szalloda:
    def __init__(self, nev):
        pass

    def add_szoba(self, szoba):
        pass

    def listaz_szobak(self):
        pass

# Foglalás osztály létrehozása
class Foglalas:
    def __init__(self, szoba, datum):
        pass
