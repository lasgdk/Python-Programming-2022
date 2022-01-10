# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Overordnede udtrykstyper/expressions: Assignments, aritmetiske, metodekald, deklarationer
# Husk at køre Pythons stavekontrol (inklusiv PEP8 kontrol), som bl.a. fikser
#  min manglende whitespace omkring "=" herunder:

var1 = "hej"
var2 = "med"
var3 = "dig"

# Strengkonkatenation:
print(var1 + var2 + var3)

sammenklistret_var = var1 + var2 + var3
print(sammenklistret_var)

# Aritmetisk eksempel:
print("10 + 20")
print(10 + 20)

print("10 - 20")
print(10 - 20)

print("10 * 20")
print(10 * 20)

print("10 / 20")
print(10 / 20)

# Outputtet af divisioner er kommatal:
print(type(20 / 3))

# Hvis én matematisk komponent indeholder kommatal, så bliver øvrige tal og resultatet oversat til kommatal:
print(10 + 10.5)
print(type(10 + 10.5))
# Bemærk at Integers/heltal i Python kan være enormt lange. Kommatal kan ikke være helt så lange! (128bit vist nok)

# Hvis jeg vil gennemtvinge at en division holder sig i heltal, så kan man bruge //:
print(5 // 2)
# Kan også lave heltalsdivision med kommatal, men så er resultatet også et kommatal:
print(5.1 // 2.1)

print(5 % 2)  # Og Modulus, "resten"
print(5 ** 2)  # Og opløftet i

# Og man kan bruge strenge sammen med beregningerne:
print("Hej" * 5)

# Python har en operatorpræcedens:
print(2 + 4 * 3 / 8)
# Men det er mere læsbart og "rigtigt" at bruge parenteser:
print(2 + ((4 * 3) / 8))
# Ved lange statements kan der laves mellemregninger for læsbarheden:
gang=4*3  # Først så ganger vi
brøk=gang/8  # Og så dividerer vi
sum=2+brøk  # Og så lægger vi til
print(sum)

# Vi kan tælle længden af en streng:
print(len('Hvor lang er jeg? (hint: 28)'))

# Lav en test på om noget er i en streng og returnér en boolsk værdi:
print("hej" in "hej med dig")  # Tester om hej er i strengen, og returnerer True eller False
print("verden" in "hej med dig")  # Tester om hej er i strengen, og returnerer True eller False

# Man kan køre en snippet (markering) af kode med Shift+Alt+e

# Konvertere fra en datatype til en anden:
str(10)  # Integer 10 konverteres til en streng, "10"
type(str(10))

int('10')  # Lav strengen '10' om til heltallet 10
type(int('10'))

# Brugerinput via input() gemmes som udgangspunkt altid som strenge. Så her angives det eksplicit at gemmes
#  som et heltal i stedet:
user_input_int = int(input("Skriv et tal: "))
print(user_input_int)
print(type(user_input_int))

# "modtager"-typen skal naturligvis kunne holde dataen, så f.eks. denne duer ikke:
# int("10.123")
# Men denne duer fint:
float("10.123")
complex("5+7j")

