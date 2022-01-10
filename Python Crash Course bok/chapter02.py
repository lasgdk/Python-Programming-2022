message = "Hej verden"
print(message)


# Strings kan nemt ændres til f.eks. "Title Case", "UPPERCASE" eller "LOWERCASE":
name = "LArs sommer"
print(name.title())
print(name.upper())
print(name.lower())
# Især "lower" er smart til at opbevare data i, hvis man generelt er ligeglad med casen.

# "format strings" med f foran variablerne kan sætte flere variable sammen, f.eks.:
fornavn = "lars"
efternavn = "sommer"
fulde_navn = f"{fornavn} {efternavn}"
print(fulde_navn)
velkomstbesked = f"Hej, og velkommen til {fulde_navn.title()}"
print(velkomstbesked)

# whitespace i strenge kan tilføjes med f.eks. \n og \t:
sprog = "\nprogrammeringssprog:\npython\nc\nassembler"
print(sprog.title())
fleresprog = "\nsprog:\n\tdansk\n\ttysk\n\tnedertysk"
print(fleresprog.title())

# funktionerne strip, lstrip og rstrip kan fjerne whitespace i start og slutning af strenge:
pladderinput = "  hej verden   "
print(pladderinput)
print(pladderinput.strip())

# heltal:
print(2 + 5)
print(2 - 5)
print(2 * 5)
print(2 / 5)

# Husk at floats giver approksimater:
print(0.2 + 0.1)

# Ved store tal kan man indsætte underscores for læsbarheden. De kommer ikke med i beregningerne:
print(1_000_000 + 2_000_000)

# Man kan assigne flere variable i samme linje, så længe antallet af variable og værdier er ens:
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

# Konstanter findes ikke i python, men for læsbarhedens skyld skrives variable der ikke tænkes ændret med stort:
MAX_CONNECTIONS=1000

# Zen of Python kan listes med denne:
import this
