# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Kontrolstrukturer og sammenligninger

# Evaluer om det er lig med
print(10 == 10)    # True
print(10 == 20)    # False

# Evaluer om det IKKE er lig med
print(10 != 10)    # False
print(10 != 20)    # True

print(1 < 5)
print(2 > 10)
print(1 <= 1)
print(2 >= 0)

# Floating points er FLYDENDE, så de kan ikke sammenlignes så nøjagtigt, f.eks.:
print(3.3 == 3.3)   # True
print(3.3 == (1.1 + 2.2))   # False, fordi floating points ikke er præcise når man bruger aritmetiske funktioner på dem!

# Så sæt nogle tolerancer for floating pointsne:
x = (1.1 + 2.2)
tolerance = 0.000001
if x > (3.3 - tolerance) and x < (3.3 + tolerance):
    print("Ja, nu er de så godt som ens :-)")
    print(3.3)
    print(x)


# Or og And:
# Or skrives som "or"
# Xor skrives som "^"
if True or False:
    print("Altid!")
if True ^ False:
    print("Også altid")
if True and True:
    print("Også altid")
if not False:
    print("Også altid")


# Nestede kontrolstrukturer:
trylletallet=8
if trylletallet > 4:
    if trylletallet < 10:   # Man kan indsætte flere nestede kontroller
        print("Er det måske 8?")
    else:
        print("Det er nok ikke 8..")
else:
    pass    # Placeholder/tom kommando, nogle gange en placeholder for senere kode.
# Og så er der også elif, "Else, if;"
# I dag er der for nyligt også kommet en switch-case kontrolstruktur i Python

