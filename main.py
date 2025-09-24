# Funkcija za učitavanje teksta iz datoteke
def ucitaj_tekst(filepath):
    try: 
        # tu ide logika za citanje datoteke
        with open (filepath, 'r', encoding= 'utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Datoteka '{filepath}' nije pronađena.")
        return None

# Funkcija za pročišćavanje teksta
def ocisti_tekst (tekst):
    # Kod za pročišćavanje teksta ide ovdje
    tekst = tekst.lower()
    return tekst

if __name__== "__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)
    if ucitani_tekst:
        print("Ucitani tekst je:")
        print(ucitani_tekst)
    else:
        print("Greska pri ucitavanju datoteke")
    ucitani_tekst = ocisti_tekst(ucitani_tekst)
    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)
    else:
        print ("Greška pri očišćavanju teksta.")

