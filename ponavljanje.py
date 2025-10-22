"""
broj = 10 #integer
ime = "pero" #string
znak = 'a' #carachter (char)
cijena = 10.5 #float (decimalan broj)
istina = True #bool (boolean)
"""

#zadatak 1
"""""
if broj > 5:
    print("Broj je veći od 5.")
elif broj  == 5:
    print("Broj je jednak 5")
else: 
    print("Broj nije veći od 5")

if istina:
    print("True")
else:
    print("False")
"""

#zadatak 2
"""
print("unesi temp:")
temp = input()
temp =int(temp)


temp = int(input("Unesi temp"))
if temp <=0:
    print("ledenicaaa")
elif temp >0 and temp <=15:
    print("hladno")
elif temp >15 and temp <=25:
    print("ugodno")
else:
    print ("vrućee")
"""

#petlje
""""
for i in range(10):
    print (i)

for slovo in "Bok":
    print(slovo)

brojac = 0
while brojac < 11:
    print(brojac)
    brojac += 1
"""

#zadatak 3

for broj in range(2, 21):
    if broj % 2 == 0:
        print(broj)
    else:
        continue

for broj in range (2,21,2):
    print (broj)

while broj <=20:
    print(broj)
    broj += 2
