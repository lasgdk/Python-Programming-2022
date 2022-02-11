# Noget om dictionaries

trussel1={'mod': 'fortrolighed', 'cvss': 6}
print(type(trussel1))
print(trussel1)
print(trussel1['mod'])
print(trussel1['cvss'])

# Værdier kan naturligvis både behandles og sættes i nye variable:

aktuel_cvss=trussel1['cvss']
print(f"Wow, den nuværende CVSS er {aktuel_cvss}!")

# Nye key-value-par kan sættes ind i dicts:
trussel1['relevant'] = True
trussel1['haandteret'] = False
print(trussel1)

# Hvis dicts bruges sådan, hvor nye key-value-sæt indsættes, og dict'en ikke er initialiseret før,
#  skal den startes som en tom dict:
trussel2={}
trussel2['relevant'] = False
trussel2['haandteret'] = False
print(trussel2)

# Dicts kan bare lige få ændret værdier:
trussel1['haandteret'] = True
print(trussel1)