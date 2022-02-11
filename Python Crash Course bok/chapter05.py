# afsnit 5 om if-sætninger

biler = ['volvo', 'bmw', 'ford']
for bil in biler:
    if bil == 'bmw':
        print(bil.upper())
    else:
        print(bil.title())

# Vi kan teste for lighed:
bil='ford'
if bil == 'ford':
    print('Jep, de er ens')

# Gæt tallet-spil-ish med nogle if-sætninger

hemmeligt_tal=5
input_tal=5 # Sat til 5 for at springe nedenstående over når det hele bare køres..
while hemmeligt_tal != input_tal:
    input_tal=int(input('smid mig et tal:'))
    print('Du skrev '+str(input_tal))
    if input_tal<hemmeligt_tal:
        print('Det indtastede tal er lavere end det hemmelige tal, prøv igen')
    elif input_tal>hemmeligt_tal:
        print('Det indtastede tal er højere end det hemmelige tal, prøv igen')
    elif input_tal==hemmeligt_tal:
        print('Yaay, du gættede det!')

# Vi kan slå op om noget er i en liste:
print('ford' in biler)  # Den giver True
print('bazinka' in biler)  # Den giver False

nybil='mazda'
if nybil not in biler:
    biler.append(nybil)
print(f"{biler[-1].title()} er nu med i bilparken!")

# Boolske udtryk kan også bruges til at sætte ja/nej-variable:
spillet_er_aktivt=True
brugeren_kan_redigere=False

