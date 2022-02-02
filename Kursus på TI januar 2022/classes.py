
class Dog:
    kind='Canine'   #Oprettes i namespace der er delt med alle instanser af klassen

    def __init__(self, name, race): #Kræver at navn og race angives når der laves en instans af klassen
        self.name = name    #Oprettes i namespace der er unik for hver instans af klassen
        self.race = race
    def __repr__(self): #Kaldes hvis instansen af klassen kaldes, f.eks. med print(fido)
        return f"Dog({self.name}, {self.race})"


fido=Dog('Fido', 'Labrador')    #Lav en instans af Dog der hedder fido

print(type(fido))   #Klasse: Dog

print(fido)
print(fido.kind)
print(fido.race)

