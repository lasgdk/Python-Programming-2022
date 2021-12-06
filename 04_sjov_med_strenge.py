# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut
# Sjov med strenge

# Husk at en streng bare er en kollektion af tegn

demostring = "Hej med jer, her er en streng i Python :-D"
# Index:      0123456789...

# Tag fat i tegn nummer 4 i strengen: (husk vi starter med nummer 0)
print(demostring[4])

# Tag fat i tegn 4 og indtil og uden 7:
print(demostring[4:7])  # Fra-og-med, til-og-ikke

# Tæl bagfra i stedet, og tag fat i tegn nummer 3 fra højre:
print(demostring[-3])  # Bagfra tælles fra -1, og ikke fra 0

# Tag fat i alt undtagen de tre sidste:
print(demostring[0:-3])

# Smileyen alene, altså de sidste tre tegn:
print(demostring[-3:len(demostring)])
# Denne gør det samme, da ingen specificering betyder "til resten" eller "fra første":
print(demostring[-3::])

# Så default med/uden specificering:
# demostring[0:len(demostring):1] er det samme som:
# demostring[:::]

# Starter ved -4 (ovre mod højre), og går mod 0, men 0 er passeret, så denne gør ikke spor:
print(demostring[-4:0])

# Starter ved -4 (ovre mod højre), og går mod 0, men -1 siger at pegepinden skal gå i den anden retning
print(demostring[-4:0:-1])

# At arbejde med strenge denne måde hedder slicing, og hvert trin hedder strides

# Tag hvert andet tegn:
print(demostring[::2])
# Eller hvert tredje:
print(demostring[::3])
# Osv..
print(demostring[::4])
print(demostring[::5])
print(demostring[::6])

