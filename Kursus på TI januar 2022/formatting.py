
# Strenge kan formateres med f.eks. %s og %d, hvor strengen og nummeret så indsættes.
print("Jeg hedder %s og er %d år gammel" % ("Lars", 23))

# Men mere dynamisk kan det laves med denne måde:
print("Jeg hedder {} og er {} år gammel" .format("Lars", 23))

# Objekterne kan godt ændre rækkefølge hvis relevant, ved at sætte tal i {};
print("Jeg hedder {1} og er {0} år gammel" .format("Lars", 23))

# Ved at angive : og tal i {}'erne, kan der angives hvor mange tegn der skal afsættes til hver af dem. 
print("Jeg hedder {:10} og er {:10} år gammel" .format("Lars", 23))
# Strings er venstrestillede, så navnet der er en string rykkes mod venstre. Tal er højrestillede, så de 23 kommer til højre i de 10 felter.

# Det kan midterstilles med ^, se:
print("Jeg hedder {:^10} og er {:10} år gammel" .format("Lars", 23))

#Formattering kan også laves med:
navn='Lars'
alder=123
print(f'Jeg hedder {navn} og er {alder} år gammel')

