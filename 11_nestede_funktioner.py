# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Funktioner i funktioner, generelt dårlig stil!

def ydrefunktion():
    print("Dette er den ydre funktion")
    def indrefunktion():
        print("Dette er den indre funktion")
    indrefunktion()
ydrefunktion()
# indrefunktion() kan naturligvis ikke kaldes her, da den kun er defineret inde i ydrefunktion.

