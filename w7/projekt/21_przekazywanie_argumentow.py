"""
Wykład 7 — slajd „Przekazywanie argumentów”
Plik: 21_przekazywanie_argumentow.py

Parametr dostaje referencję do obiektu: przypisanie zmienia tylko lokalną nazwę,
metoda modyfikująca zmienia obiekt wywołującego; += na liście działa w miejscu.
"""

def rebind(xs):
    xs = [0, 0]         # nowa lista – lokalna nazwa
def mutate(xs):
    xs.append(0)        # zmiana obiektu wywołującego
def extend(xs):
    xs += [9]           # lista: += działa w miejscu!
def increment(n):
    n += 1              # int niezmienny – nowy obiekt
    return n

a = [1, 2]
rebind(a)
print(a)
mutate(a)
extend(a)
print(a)
k = 5
print(increment(k), k)


# --- Oczekiwany wynik ----------------------------------------
# [1, 2]
# [1, 2, 0, 9]
# 6 5
