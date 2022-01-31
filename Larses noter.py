# Beregninger; / er division, men // er heltalsdivision og % er modulus(resten), f.eks.
from tkinter import Y


print(17/5)
print(17//5)
print(17%5)


# Python er et typestærkt sprog, men kan nemt skifte type på variable.
# Python kan lave implicit konvertering af tal, mellem heltal og kommatal;
3 * 3.5 -1

# I interaktiv modus, hvor fortolkeren står klar med ">>>", kan "_" bruges som reference til det sidst evaluerede. Det kan ikke anvendes sådan i scripts.
# I scripting modus kan "_" bruges til to andre ting, de kommer senere.

# Komplekse tal:
print(0.7+0.7j)
print((0.7+0.7j) ** 2)
print((0.7+0.7j) ** 2 **2 )


# Quotes:
print('"Isn\'t it great?!" they said')

# newlines and similar:
print("hej\nverden")
print("hej\tverden")

# Et dårligt forsøg på en path:
path="C:\temp\newfile.txt"
print(path)

# Løsning på den dårlige path:
# Sæt r foran strengen, for at fortælle det er en "Raw string":
path=r"C:\temp\newfile.txt"
print(path)
# Eller en bunke escapes:
path="C:\\temp\\newfile.txt"
print(path)

# Strings med gentagelser og tilføjelser, et skørt grundstof:
print(3 * 'un' + 'ium')

# To strenge lige ved siden af hinanden, bliver bare sammensat:
print('sammen''satte'' strenge')

# strenge kan strækkes over flere linjer:
print('Her er noget tekst, '
'og mere tekst, '
'og så lidt til...')

# strenge er indexable/indeksérbare:
word="python"
# Indexer:
print(word[1])
print(word[-1])
# Slicing:
print(word[0:3]) # Tegn 0 til før 3
print(word[3:5]) # Tegn 3 til før 5
print(word[-3:]) # Sidste tre
# Ved indexering får man fejl hvis man addresserer udenfor range. Men ved slicing kan man godt gå udenfor:
print(word[3:42]) # Tegn 3 til før 42

# Strenge er immutable, dvs. kan reelt ikke ændres. Men man kan lave en ny streng i stedet.
# Så man kan ikke tildele/ændre strenge ved at indexere eller slice.
# Men man kan lave en ny streng, og tage dele af den gamle, f.eks.:
print('J'+word[1:])
print(word[0:3]+'test')


# Sektion 3.1.3 i manualen: Lists

# Hovsa med lister:
liste1=[1,2,3]
liste2=liste1 # Man kunne tro at liste2 bliver en kopi af liste1, men det gør det ikke! Den bliver bundet til liste1!
liste1[1]=22
print(liste1)
print(liste2) # Se det går galt her, hvor 22 også er i liste2
print(id(liste1), id(liste2)) # id printer objekt-id, som her er ens.

# I stedet skal der laves en ny liste, f.eks. med at slice hele liste1:
liste2=liste1[:]
liste1[1]=42
print(liste1) # NU er det kun liste1 der ændres
print(liste2) # Så liste2 er stadig sin egen, og ikke ændre med 42.
print(id(liste1), id(liste2)) # id printer objekt-id, som NU er forskellige

# == sammenlign om det er to ens, "har vi to ens trøjer på?"
# "is", sammenlign om det er det samme, "har vi den samme trøje på?"
# før kunne tjekkene på listerne også laves med:
print(id(liste1) == id(liste2))
print(id(liste1) is id(liste2))

# Vi sætter dem ens igen:
liste2=liste1
print(id(liste1) == id(liste2))
print(id(liste1) is id(liste2))

# lists er mutable, dvs. vi kan "bare lige" appende, ændre osv i listerne.

liste1+=[5]
print(liste1)
print(liste2)
# Nu har begge lister fået 5 med sig.

liste1.append([6])
print(liste1)
print(liste2)
# Nu har begge lister fået 6 med sig.


# Lister kan indeholde lister:

listeliste1=[[1,2,3],[4,5,6]]
listeliste2=listeliste1
listeliste3=listeliste1[:]
print(str(listeliste1) +' id: ' + str(id(listeliste1)))
print(str(listeliste2) +' id: ' + str(id(listeliste2))) # listeliste2 er samme id som listeliste1
print(str(listeliste3) +' id: ' + str(id(listeliste3))) # listeliste3 er en kopi af listeliste1, MEN det er listerne inde i listeliste ikke!

print(str(listeliste1[0]) +' id: ' + str(id(listeliste1[0])))
print(str(listeliste2[0]) +' id: ' + str(id(listeliste2[0])))
print(str(listeliste3[0]) +' id: ' + str(id(listeliste3[0]))) # SE her er id de samme på alle tre, for der er kun lavet shallow copy.
# BEMÆRK at listernes liste ikke kopieres, men kun refereres! 
# Det er fordi selv med linjen der slices listeliste1 ud i listeliste3 laves der kun Shallow (ikke-dyb kopi)
# Skal der laves dyb kopi, rigtig kopi, hele vejen ned i listerne, skal der anvendes funktionen deepcopy fra et library.

# Hvis det kan overskues, kan hver listeliste også slices ud sådan her:
listeliste3[0]=listeliste1[0][:]
print(str(listeliste1[0]) +' id: ' + str(id(listeliste1[0]))) 
print(str(listeliste3[0]) +' id: ' + str(id(listeliste3[0]))) # Nu er id forskellige


# Et par sammenligninger:
tekst="her er noget tekst"
print("nog" in tekst) # Er der "nog" i tekst? Ja.


# Print slutter som udgangspunkt med ny linje, men kan justeres med "end", f.eks.:
a=0
while a < 5:
    print(a, end=", ")
    a=a+1

# Print multiplication table nicely:
print()
print("Print multiplication table nicely:")
max_x=5
max_y=5
for y in range(1, max_y + 1):
    for x in range(1,max_x + 1):
        prod=x*y
        outstr = "{:4} ".format(x*y)
        print(outstr, end="")
    print()

# Syvtals-bum-leg. Erstat tallet med "bum" hvis det indeholder 7 eller er deleligt med 7:
for n in range(1, 101):
    if (n % 7 == 0) or ('7' in str(n)):
        print("bum", end=", ")
    else:
        print(n, end=", ")


print()
# Sektion 4
# Kontrolstrukturer
# if-konstruktioner kan bestå af if, elif og else, men elif og else kan udelades efter behov.
liste1=[]
if liste1:
    print("liste1 indeholder noget.")
else:
    print("liste1 indeholder ikke noget")
print()


# For-konstruktion:
ordliste=['kat', 'hund', 'hest']
for ord in ordliste:
    print("Ordet er: \'"+str(ord)+"\' og længden af ordet er: "+ str(len(ord)))

# For med Ranges:
for i in range(len(ordliste)):
    print("Ordet \'"+str(ordliste[i])+"\' er på denne position i listen: "+str(i))

# Men for at slå de to ovenstående sammen, er det smartere at bruge enumerate:
for i, ord in enumerate(ordliste):
    print("Ordet er: \'"+str(ord)+"\' og længden af ordet er: "+ str(len(ord)) +" og positionen af ordet i listen er: "+str(i) )

# objekterne range og enumerate er "dovne" objekter, da de først bliver til noget når vi bruger dem.
range(1,10000000000000000000000000000000000000000000) # er harmløst indtil vi begynder at bruge det

# lister og ranges og strenge er "iterable", dvs. vi kan iterere igennem dem én ad gangen:
for tegn in "hej verden!":
    print(tegn, end="")

print()
# Sektion 4.4
# I for-konstruktioner kan continue og break og else også bruges:
navne=['hans','jens','lars','kurt','bent']
for navn in navne:
    print(navn)
    if navn == "lars":
        print("Jeg fandt Lars! Stopper her..")
        break
    else:
        print("Hov, Lars er ikke her")
else: # Denne else udføres kun hvis der IKKE har været anvendt break i for-loopet
    print("Hov, Lars er slet ikke i listen")
print()


# pass kan bruges som en slags no-op:
def funktion1():
    """Dokumentationsstreng der siger noget om hvad funktionen gør"""
    pass
funktion1() # funktionen kan fint kaldes, men den gør ingenting.
help(funktion1)

def funktion2():
    raise NotImplementedError("Hov funktionen mangler jo!")
#funktion2() # funktionen kan fint kaldes, men nu kalder den en fejl hvis funktionen køres

# Sektion 4.7.1: Når man skriver funktioner, kan det være smart at lave defaultværdier på argumenterne, hvis ikke alle udfyldes.
# def minfunktion(arg1, arg2="Dette er default!")
# funktioner kan tage et vilkårligt antal argumenter med *,
# def opsummer(*alleinputtal)
# se også eksempel i sektion 4.7.2
# Special parameters i sektion 4.7.3 giver god mening hvis man læser help til print f.eks.,
#  hvor nogle argumenter skal være keyword, og nogle skal være positionelle

# første argument skal være positionel, andet argument kan være enten eller, tredje argument skal være keyword:
def funktion(kunpositionel, /, entenpositionelellerkeyword, *, kunkeyword):
    return
funktion(1, entenpositionelellerkeyword="Det er okay", kunkeyword="Det er okay")
funktion(1, "Det er okay", kunkeyword="Det er okay")

# Man kan "unpacke" en liste med en * foran:
def opsummer(*allemuligeinput):
    res=0
    for a in allemuligeinput:
        res+=a
    return res
talliste=[1,2,3,4,5]
print(opsummer(*talliste))

# Via ** kan man sende tupler af data til en funktion og pakke det ud:
def hello(name,timeofday):
    print("Hej "+name+", good "+timeofday)
# tuple af data:
data = {'name': 'Lars', 'timeofday': 'afternoon'}
hello(**data)

#Lambda-funktioner kan lave små funktioner ud af en funktion:
def make_incrementor(n):
    return lambda x: x+n
f42=make_incrementor(42) # bygger en funktion der lægger noget til 42
print(f42(8))
f100=make_incrementor(100) # bygger en funktion der lægger noget til 100
print(f100(8))

# Dokumentationsstrenge kan kaldes via help, men også via print og lign.:
help(funktion1)
print(funktion1.__doc__)

# Python virker okay med unicode. Dog ikke til alt:
# Virker ikke:
# 🙂=5
# print(🙂)
# Also not working: 
# liste=[😆,🤣,😀,🙂,😉]
# print(liste)
# Men vi kan godt printe disse her:
# Ved at angive unicode koder:
# grinning face
print("\U0001f600")
# grinning squinting face
print("\U0001F606")
# rolling on the floor laughing
print("\U0001F923")
# Ved at angive navne:
# grinning face
print("\N{grinning face}")
# slightly smiling face
print("\N{slightly smiling face}")
# winking face
print("\N{winking face}")
# Disse virker også fint:
print("🙂")
print("🤣")
print("😀")
print("😉")

# Her er en stribe unicodes:
for i in range(0,110):
    print (i, chr(i))
for i in range(128510,128519):
    print (i, chr(i))


# Datastrukturer i Python. Sektion 5. Der er fire typer:
# lister, tupler, set, dictionaries

# en liste er dobbelthægtet, dvs. en given placering "hænger sammen med" forrige og næste,
#  altså man kan nemt addressere en given placering, samt den før, den efter, osv.
print()
liste1=[1,2,3]
print(liste1)

liste1.append(6) # Tilføj ét item
print(liste1)

liste1.extend(range(7,10)) # Tilføj noget i flertal
print(liste1)

liste1.insert(3,4) # Insæt 4 efter placering nummer 3
print(liste1)

liste1.remove(9) # Fjern tallet 9, hvis det er til stede
print(liste1)

print(liste1.pop()) # Fjern (pop) sidste item i listen, og arbejd med det.
print(liste1)
print(liste1.pop(1)) # Fjern (pop) placering 1 item i listen, og arbejd med det.
print(liste1)

liste1.reverse() # Vend listen om og gem den
print(liste1)

liste1.append(1)
print(liste1)
print(liste1.count(1)) # Tæl hvor mange gange værdien 1 fremgår af listen (2 gange her)

print(sorted(liste1)) # Viser en sorteret udgave af liste1, men uden at ændre på selve listen. sorted er en funktion.
print(liste1) #Listen er stadig i rodet rækkefølge
liste1.sort() #Sorterer, kan tage f.eks. reverse og keys som input, og gemmer listen. sort er en metode på en liste.
print(liste1)

print(liste1.index(3)) #Find på hvilken position i listen at værdien forekommer. Værdi 3 står på plads 2

del liste1[0] # Fjerner et element i en liste
print(liste1) 

liste1.clear() # Tøm listen
print(liste1)

# Via append og pop kan lister bruges ligesom en alm. stak hvor man pusher og popper.
# Men hvis man vil bruge lister til køer/queues, er modulet collections.deque optimeret til det meget mere.


# List comprehension, en nem måde at bygge en liste på:
liste1=[x**2 for x in range(10)]
print(liste1)
# liste med tal der ikke er delelige med 3:
liste2 = [x for x in range(100) if x%3!=0]
print(liste2)
# eller bare tal derudaf:
liste3 = [x for x in range(10)]
print(liste3)


# Tupler er en anden form for rækkefølge end lister, selv om der er mange ligheder.
# Tænk som udgangspunkt at lister bør være heterogene værdier, f.eks. højder eller vægt over en række personer
# Tænk som udgangspunkt at tupler bør være sammenhængende værdier, f.eks. parametre for en person, herunder højde, vægt mm.

tuple1=1,2,3
print(tuple1)
print(type(tuple1))
# Men en tuple er immutabel, dvs. vi kan ikke ændre en given placering, f.eks. tuple1[0]=123 virker ikke.
tomtuple=()
tuplemeden='ét element',

# Man kan udpakke tupler til diskrete variable:
x, y, z = tuple1
print(x, y, z)
# og pakke dem sammen igen:
tuple2 = (x, y, z)
print(tuple2)

# Set, altså samlinger eller mængder, er en usorteret/uordnet bunke af elementer
# Alle elementer er unikke i set. De bruger til at undersøge om noget er med eller ikke med, til at fjerne dupletter mm.
# union, fællesmængde
# intersection, foreningsmængde

