import math

a = int(input("Podaj długość pierwszej przyprostokątnej trójkąta: a = "))
b = int(input("Podaj długość drugiej przyprostokątnej trójkąta: b = "))

c = math.sqrt(pow(a, 2)+pow(b, 2))

print(f"Dla podanych boków, przeciwprostokątna równa się c = {c:.0f}")