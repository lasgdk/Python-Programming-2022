# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Funktioner

def min_første_funktion():
    pass

# Definér en funktion:
def printhej():
    print("Hej med dig!")
# Og kald funktionen:
printhej()
printhej()
printhej()

# Giv input til en funktion:
def printnavnet(name):
    print("Hej " + name)
printnavnet("Lars")
printnavnet("Jens")
printnavnet("Hans")

# Og lidt funktion med input og en "hvis" i en streng:
def printnavnet(name):
    if "a" in name:
        print("Hey "+ name + ", der er et a i dit navn!")
    else:
        print("Hej " + name)
printnavnet("Lars")
printnavnet("Jens")
printnavnet("Hans")

# Funktioner med input kan have en defaultværdi, f.eks.:
def tæloptil(til = 10):
    for a in range(1,til):
        print(a)
tæloptil(5) # Sætter 5 som input
tæloptil()  #Intet input, defaulter derfor til de 10


# Bemærk det er dårlig kodestil at bruge samme funktionsnavn flere gange, som netop gjort herover.
del printnavnet
del tæloptil


# Scope og funktioner:

# Inde i funktioner arves variable uden for funktionen:
x = 10
def funktion():
    print(x)
funktion()

# Men udenfor funktionen "ud-arves" variablen ikke:
z=5
def funktion():
    z = 10
funktion()
print(z)

# Men inde i en funktion kan en variabel udenfor godt sættes eller ændres, med keyword "global":
z=5
def funktion():
    global z
    z = 10
funktion()
print(z)


# En familiefunktion med mange input:
def familiefunktion(navn1,navn2,navn3):
    print(navn1)
    print(navn2)
    print(navn3)
familiefunktion("Jens","Hans","Lone")
# Det kan være svært at holde styr på hvad der er hvad af inputvariable.
# Så de kan anføres mere eksplicit:
familiefunktion(navn1="Jens",navn3="Hans",navn2="Lone")

# Når man i funktioner begynder at definere default-argumenter i input, så skal ALLE derefter have default-værdier:
# F.eks.:
# familiefunktion(navn1,navn2,navn3="Jens") er lovligt
# mens:
# familiefunktion(navn1,navn2="Jens",navn3) er ulovligt
# men kan gøres lovligt med:
# familiefunktion(navn1,navn2="Jens",navn3="") er lovligt

