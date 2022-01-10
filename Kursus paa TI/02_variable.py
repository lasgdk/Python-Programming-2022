# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Variable i Python

# Helt enkelt:
# x=10
# print(x)

# Navngivning: VariableMåGerneHaveLangeNavne_SåDeFortællerHvadDeHandlerOm = 10 Men det er dårlig stil at anvende
#  non-ascii-chars til dem
ItIsBadPracticeToWriteInNonEnglishTheTeacherSays = 5
UseLargeLetterToSeparateWords_or_use_something_else_eg_underscores = 2
# Variable kan ikke starte med tal, f.eks. 1variable=20
# Heller ikke indeholde f.eks. , eller .
# Vælg en konvension for navngivning, f.eks. VariableName eller variable_name
# Python "officiel" guide, PEP8: lowercase_separated_by_underscore

# Variable kan tage input fra brugeren:
print('Giv et input til datamaten:')
user_input = input()
print("The user wrote: " + user_input)

# Input kan også udvides med en tekst til brugeren direkte i input-linjen:
print('Giv et nyt input til datamaten:')
user_input2 = input("Inputlinjen er her, skriv her: ")
print("The user now wrote: " + user_input2)

# Variable kan slettes igen med:
del user_input
del user_input2

# Datatypen kan ændres "bare lige":
testvariable1=10
print(type(testvariable1))
testvariable1="Nu er jeg en string"
print(type(testvariable1))

