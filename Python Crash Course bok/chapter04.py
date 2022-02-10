# Chapter 4, working with lists

# at loope gennem en hel liste:
naboer = ['jens', 'peder', 'lone']
for nabo in naboer:
    print(nabo)

# Lidt formattering undervejs:
for nabo in naboer:
    print(f"{nabo.title()}, hedder min ene nabo!")

# Hvis der er brug for en simpel liste med en talrække, kan den laves med range():
for v in range(1, 5):
    print(v)

tital=range(1, 11) #Liste med ti tal
for tal in tital:
    print(tal)

# Range kan bruges i steps også, f.eks. hvert andet tal (de lige):
print('Lige numre:')
for tal in range(2, 11, 2):
    print(tal)

# Man kan naturligvis arbejde med tallene, f.eks. finde deres kvadrattal og gemme i en ny liste:
kvadrater=[]  # initialiserer listen
for tal in range(1, 11):
    kvadrater.append(tal ** 2)
print(kvadrater)

# Man kan lave simpel statistik med lister:
tital=range(1, 11)
print(min(tital))
print(max(tital))
print(sum(tital))

# list comprehension er en måde at skrive nogle af ovenstående i én linje:
kvadrater = [tal ** 2 for tal in range(1, 11)]
print(kvadrater)

kuber = [tal ** 3 for tal in range(1, 11)]
print(max(kuber))
print(sum(kuber))

opisigselvhvadhedderdetnu = [tal ** tal for tal in range(1, 11)]
print(opisigselvhvadhedderdetnu)

# Hvis man arbejder med et stykke af en liste hedder det en slice. At tage et stykke liste hedder at "slice"
print(naboer)
print(naboer[0:2])  # slice fra position 0 til lige før 2
print(naboer[1:3])  # slice fra position 1 til lige før 3
print(naboer[:2])  # Uden startangivelse startes også fra 0. slice fra position 0 til lige før 2
print(naboer[1:])  # Uden slutangivelse køres helt ud. slice fra position 1 til slut
print(naboer[-2:])  # de sidste to

# der kan loopes igennem en slice:
print('Her er de sidste to naboer:')
for nabo in naboer[-2:]:
    print(nabo.title())

# at kopiere lister:
en_andens_naboer = naboer  # FORKERT!! Der laves kun en soft copy, en slags henvisning, til det samme data.
print(id(en_andens_naboer))
print(en_andens_naboer)
print(id(naboer))
print(naboer)
naboer.append('bent')  # Man kunne tro at den kun tilføjes i den ene liste, men nej, det er ikke tilfældet:
print(en_andens_naboer)
print(naboer)

# I stedet skal listen løbes igennem og hvert item skrives i en ny liste:
en_andens_naboer = naboer[:]  # Kopierer fra slice 0 til slice slut.

naboer.append('bente')  # Og SÅ virker det som måske først tilsigtet.
print(id(en_andens_naboer))
print(en_andens_naboer)
print(id(naboer))
print(naboer)

# Lister er mutable, dvs. til at ændre/mutere. Nogle gange har vi brug for lister der ikke er det.
# Det er tupler. Tupler er lister der er immutable.

de_permanente_tal = (10, 20)
print(de_permanente_tal)
print(type(de_permanente_tal))
print(de_permanente_tal[0])
print(sum(de_permanente_tal))

# Tupler kan naturligvis overskrives, men ikke modificeres med f.eks.
# de_permanente_tal[0] = 123

# Men overskrives f.eks.:
de_permanente_tal = (123, 234)

print('Vores gode og faste menukort:')
det_permanente_menukort = ('bøf', 'pasta', 'mere pasta')
for mad in det_permanente_menukort:
    print(mad.title())

