# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

"""
Opgave:
Lav en regnemaskine, der tager input fra terminal, to tal og en operator
Skal køre i en løkke, med en afslutte-funktion
Bonuspoint hvis regnestykket kan stå på én linje, og det parses rigtigt
"""

# Super simpel løsning:
# print(eval(input()))


print("Velkommen til regnemaskinen hvor tal og operatorer skal indtastes per linje!")
while True:
    tal1=input("Skriv første tal (skriv x for at afslutte): ")
    if tal1 == "x":
        break
    print("Ok, første tal er: "+str(tal1))
    tal2 = input("Skriv andet tal (skriv x for at afslutte): ")
    if tal2 == "x":
        break
    print("Ok, andet tal er: " + str(tal2))
    tal1=int(tal1)
    tal2 = int(tal2)
    operator = input("Skriv operatoren (+, -, *, /): ")
    match operator:
      case "+":
        print(tal1 + tal2)
      case "-":
        print(tal1 - tal2)
      case "*":
        print(tal1 * tal2)
      case "/":
        print(tal1 / tal2)
      case _: # Underscore her er default'en. Hvis ingen match på andet, så default til denne.
        print("Du er dårlig til at vælge mellem fire operatorer, jeg giver op..")
        break

