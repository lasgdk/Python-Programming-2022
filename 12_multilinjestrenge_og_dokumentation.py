# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Flerlinjestrenge

print("At printe et dobbeltcitationstegn: \"")

print("At printe over\
 flere linjer")

print("""Sådan her kan man
også printe mange linjer
uden at skulle bruge escapes 
hele tiden... 
Men til gengæld kommer der linebreaks med!
""")

print('''
Det virker også med 
enkeltcitationstegn''')

multilinjestrengvariabel="""
Her er en mindre fortælling
om alt muligt
Det kunne vel være en halv roman
\"\"\" tilmed med sådan en stak dobbeltcitationstegn i!
"""

print(multilinjestrengvariabel)


# Til brug i dokumentation:

def min_dokumenterede_funktion():
    """ Hvis man indsætter en streng som det ALLERFØRSTE i en funktion i Python, (og klasser?), opfattes
    det som dokumentation for funktionen, som kan opsamles af eksterne værktøjer mm.
    Her er selve dokumentationen af funktionen: Den returnerer bare 5..
    """
    return 5

# Dokumentationen i en funktion kan listes med denne:
print(min_dokumenterede_funktion.__doc__)


