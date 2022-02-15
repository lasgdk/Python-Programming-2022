# Noget om dictionaries

trussel1 = {'mod': 'fortrolighed', 'cvss': 6}
print(type(trussel1))
print(trussel1)
print(trussel1['mod'])
print(trussel1['cvss'])

# Værdier kan naturligvis både behandles og sættes i nye variable:

aktuel_cvss = trussel1['cvss']
print(f"Wow, den nuværende CVSS er {aktuel_cvss}!")

# Nye key-value-par kan sættes ind i dicts:
trussel1['relevant'] = True
trussel1['haandteret'] = False
print(trussel1)

# Hvis dicts bruges sådan, hvor nye key-value-sæt indsættes, og dict'en ikke er initialiseret før,
#  skal den startes som en tom dict:
trussel2 = {}
trussel2['relevant'] = False
trussel2['haandteret'] = False
print(trussel2)

# Dicts kan bare lige få ændret værdier:
trussel1['haandteret'] = True
print(trussel1)

# Vi kan fjerne nøgle-værdi-par fra bibliotekerne:
del trussel1['cvss']
print(trussel1)

# ved at bruge kommandoen "get" kan man teste om der er nøgler i dicten først, og ellers give en fejlbesked:
aktuel_cvss = trussel1.get('cvss', 'Der er ikke sat en CVSS på denne trussel!')
print(aktuel_cvss)  # Hvis vi bare prøvede at printe trussel1['cvss'] ville vi få en fejl i stedet, da den ikke findes

# Loop igennem alle nøgler og værdier af en dict:
for noegle, vaerdi in trussel1.items():
    print(f"\nNøglen er: {noegle}")
    print(f"Værdien er: {vaerdi}")

# Eller loope igennem nøglerne bare:
print('Nøglerne i denne dict er:')
for noegle in trussel1.keys():  # Det er faktisk default opførsel når man arbejder med en dict, så .keys() kan udelades
    print(f"Her er en nøgle: {noegle}")

# I stedet for at have parametre om forskellige ting om ét emne i én dict,
# kan man naturligvis også bruge det som en liste:
cvss_values = {
    'cve-2023-1234': 7.3,
    'cve-2024-1222': 9.3,
    'cve-2023-8534': 3.8,
    'cve-2024-1634': 5.7,
    'cve-2023-7234': 9.6,
    'cve-2024-8234': 71.3,
    'cve-2024-9234': 3.4,
    'cve-2023-1534': 4.1,
    'cve-2023-1434': 8.2,
}
business_critical = ['cve-2023-1234', 'cve-2024-1222']
for cve in cvss_values:
    print(f"Tjekker op på om {cve.upper()} har en særligt høj score eller er forretningskritisk.")
    if cve in business_critical:
        print(f"Whoa, {cve.upper()} er sandelig forretningskritisk, go fix!")
    elif cvss_values[cve] > 8.0:
        print(f"Whoa, {cve.upper()} har en mega høj score på {cvss_values[cve]}, go fix!")
# Bemærk brugen af elif her. Hvis jeg brugte "if" ville entry nummer blive opfyldt to gange,
# og begge linjer ville blive vist.
# Ved at bruge elif bliver den kun vist pga. forretningskritikaliteten.