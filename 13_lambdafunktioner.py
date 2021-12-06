# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Lambdafunktioner og lambdakalkulus
# Det er bare funktioner opfattet som data.

# Simpel funktion der bare printer en besked
def printbesked(besked):
    print(besked)
printbesked("Hej, dette er en printerfunktion")

# Jeg kan opfatte funktionen som data, og bare kopiere den over i en ny:
x=printbesked
x("Nu er jeg også en printerfunktion!")

# Her er en lambdafunktion (der ikke bruges til noget):
lambda mitegetinput : print("Hej, her er "+mitegetinput)

# Her er en lambdafunktion, der umiddelbart efter definitionen kalder sig:
(lambda mitegetinput : print("Hej, her er "+mitegetinput))(("jeg"))

# eksempel:
def lav_inkrement(n):
    return lambda x: x+n
f = lav_inkrement(10)
print(f)
f(5)
print(f)
