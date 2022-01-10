# Pythonprogrammering, 2021-12-06, Lars Sommer, Teknologisk Institut

# Fibonaccisjov
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
#  46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352,
#  24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, ...
# Fra og med det tredje fremkommer tallene som summen af de to foregående tal i følgen

# Fibonacciberegner fra underviseren, med en rekursiv funktion, meget performance-dårlig:
def beregnfibonacci(n):
    if n <= 1:
        return n
    else:
        return (beregnfibonacci(n-1) + beregnfibonacci(n-2))
antal=input("Hvor mange tal skal lægges sammen i Fibonaccirækken? Indtast her: ")
print(beregnfibonacci(int(antal)))
