# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut
# Ekstra matematik

# Numeriske værdier / Absolutte værdier:
print(abs(10))
print(abs(-10))
print(abs(-10.2))

# Find det højeste tal i en række:
print(max(1,10,100))

# Og det mindste:
print(min(1,10,100))

# Anvendt til at sanitere brugerinput:
# Her gennemtvinges et brugerinput mellem 1 og 10:
userinput=max(min(int(input("Skriv et tal mellem 1 og 10: ")),10),1)
print(userinput)

# Opstillet mere læsevenligt:
userinput=input("Skriv et tal mellem 1 og 10: ")  #Tag brugerinput
userinput=int(userinput)  # Fortolk som Integer
userinput=min(userinput,10)  # Hvis brugeren har tastet noget højere end 10, så defaulter vi ned til 10
userinput=max(userinput,1)  # Hvis brugeren har tastet noget lavere end 1, så defaulter vi op til 1
print(userinput)


