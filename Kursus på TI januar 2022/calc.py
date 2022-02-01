a = None
b = None
while True:
    try:
        if a == None:
            a = float(input("Skriv første tal: "))
        if b == None:
            b = float(input("Skriv andet tal: "))

        print("sum: "+str(a+b))
        print("difference: "+str(a-b))
        print("multiplication: "+str(a*b))
        print("division: "+str(a/b))

    except ValueError:
        print("Skriv kun heltal!")

    except ZeroDivisionError:
        print("Ikke dividere med 0! Retter dit dårlige tal til et godt tal nær 0 :-)")
        b = 2.2250738585072014e-308
    else:
        break
