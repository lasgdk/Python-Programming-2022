# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# For-løkker arbejder på en liste, på hvert element i en liste
# While-løkker arbejder til et boolsk udtryk siger stop

# Eksempel på while-løkke:
n=1
while n < 10:
    print("n er nu: "+str(n)+", udtrykket i while-loopet er "+str(n==10))
    if n == 9:
        print("Hov, men nu er n lig med 9, så NÆSTE gang while-løkken tjekker, så stopper den!")
    n=n+1   # Kan også skrives som n+=1


# Variabel-scope er anderledes i Python end i f.eks. c, så variable inde i et loop kan også bruges udenfor
if True:
    hest="pony" # Selv om variablen er sat inde i en løkke, dækker scopet også udenfor løkken.
print(hest)
# Python laver nye variabel-scopes inde i funktioner og klasser, men ikke i løkker!


# For-løkke-eksempel:
# Dét der står på højre side af "in" i en for-løkke er en kollektion, altså en samling eller række, som løkken
#  kan iterere over
for y in range(0, 10):  # range-funktionen skaber en række fra-til
    print(y)

# Manuelt ville range'n se sådan ud:
for y in [0,1,2,3,4,5,6,7,8,9]:
    print(y)

# Rækken kunne være noget helt andet:
for y in [0,1,2,"hej",4,True,6,False,8+8j,9.2]:
    print(y)

print()
print()
# For-løkkerne er smarte når der arbejdes på kollektioner, f.eks. strenge. Hvis man bare skal iterere over en
#  ensartet talrække via range(), er det nok smartere at bruge en while-løkke

# En for-løkke over en streng:
for z in "Hej med dig!":    # Itererer over hvert tegn i strengen
    print(z, end = '')

print()
print()
# En for-løkke der printer alt andet end "a"'er:
for x in "abcdefabcdef abc abc":
    if "a" == x:    # bemærk at variabelnavn og indhold kan stå lige meget på hver side af sammenligningen, selv om dette er mega grimt.
        continue    # Hvis x er et a, så spring tilbage til starten af iterationen igen.
    print(x, end = '')

print('\n')
# En for-løkke der breaker når den møder et "h":
for x in "abcdefghijklmn":
    if x=="h":
        break   # Break, hop ud af løkken og afslut den helt
    print(x, end = '')

# Break breaker kun ét niveau af løkker. Hvis man har behov for at breake i flere niveauer,
#  bør man overveje om det skulle være en funktion i stedet.


print('\n')
# Python har fået switch-case-funktion nu for nylig, men det hedder match i Python
farve='sort'
match farve:
    case "grøn":
        print("Farven er grøn!")
    case "gul":
        print("Farven er gul!")
    case "sort":
        print("Farven er sort!")
    case _: # Underscore her er default'en. Hvis ingen match på andet, så default til denne.
        print("Farven er noget andet...")
    # Hvis der ikke er en default "case _", så sker der bare ingenting hvis der ikke er match

