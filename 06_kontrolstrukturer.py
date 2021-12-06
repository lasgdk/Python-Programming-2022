# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Kontrolstrukturer

# Tre slags kontrol: Sekventiel, Selektiv/Selection, Repetetiv
# Sekventiel kontrol er når Python kører koden fra ene ende til anden
# Selektiv kontrol er når Python kun kører dele af koden, f.eks. med if-then
# Repetetiv kontrol er når Python kører noget igennem flere gange, f.eks. for-hver-element-gør, og loops, etc.

# Hav styr på dit whitespace nu! Python bruger whitespace til at vide hvad der er inde i funktioner
# Standardindrykningen er 2 eller 4 mellemrum (4 er vist en moderne tabulator)

n = 10
if n == 10:  # Dette if-statement med "==" er et boolsk udtryk (True eller False)
    print("Hej")
    print("med")  # Whitespace-indrykningen gør at linjerne hører sammen i en blok.
    print("dig")  # Det er i stedet for { } i andre sprog
print("Farvel")  # Denne er udenfor blokken

# Et if-statement kan udviddes med et else-statement:
userinput=int(input("Hvilken nummer dag i ugen er det?: "))
if userinput == 5:
    print("Det er fredag!")
else:
    print("Det er ikke fredag...")


# Hvad er sandt og falsk? True, False, sandt-agtigt, falsk-agtigt..
# 0 er falsk, tomt er falsk, alt andet er sandt
print(bool(0))  # Falsk
print(bool(0.00000000)) # Falsk
print(bool(str("")))    # Falsk

print(bool(40)) # Sand
print(bool("Hej"))  # Sand
print(bool(" "))    # Sand
print(bool(0.0000000000000000001))  # Sand






