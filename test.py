#kreiranje praznog rječnika
rjecnik = {}

print (f"Prazan rječnik: {rjecnik}")
print (f"Tip podataka je: {type(rjecnik)}")

#dodavanje elemenata: rjecnik[kljuc] = vrijednost
rjecnik['breskva'] = 5
rjecnik['jabuka'] = 10
rjecnik['banana'] = 7

print (f"Napunjeni rječnik: {rjecnik}")

#dohvaćanje vrijednosti
rjecnik['breskva'] = 5
rjecnik['jabuka'] = 10
rjecnik['banana'] = 7

print (f"Napunjeni rječnik: {rjecnik}")

rjecnik['breskva'] = 5

broj_banana = rjecnik['banana']
print (f"Broj banana je: {broj_banana}")

broj_krusaka = rjecnik
