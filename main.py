STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da']


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
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')',]
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_rijeci = tekst.split()
    return lista_rijeci


def broji_rijeci(lista_rijeci):
    brojac_rijeci = {}
    for rijec in lista_rijeci:
        if rijec in brojac_rijeci:
            brojac_rijeci[rijec] +=1
        else:
            brojac_rijeci[rijec] = 1
    return brojac_rijeci



def ukloni_stop_words(rjecnik_frekvencija, stop_words_lista):
    ocisceni_rjecnik = {}
    for rijec, frekvencija in rjecnik_frekvencija.items():
        if rijec not in stop_words_lista:
            ocisceni_rjecnik[rijec] = frekvencija
    return ocisceni_rjecnik


def sortiraj_i_ispisi(rjecnik_frekvencija, broj_rijeci=15):
    # Sortiranje po broju pojavljivanja (od najvećeg prema najmanjem)
    sortirana_lista = sorted(rjecnik_frekvencija.items(),key=lambda x: x[1],reverse=True)

    print(f"\n--- Najčešćih {broj_rijeci} riječi u tekstu ---")
    for rijec, frekvencija in sortirana_lista[:broj_rijeci]:
        print(f"{rijec}: {frekvencija}")
       

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
        #Brojanje rijeci i ispis rječnika
        brojac_rijeci = broji_rijeci(ucitani_tekst)
        print("Broj riječi u tekstu:")
        print(brojac_rijeci)
    else:
        print ("Greška pri čišćenju teksta.")
