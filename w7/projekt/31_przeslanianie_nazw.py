"""
Wykład 7 — slajd „Przesłanianie nazw wbudowanych”
Plik: 31_przeslanianie_nazw.py

Nazwy list, sum, max… można przypadkiem przesłonić — lokalnie albo, co gorsze, globalnie.
"""

def total(list):        # przesłania wbudowane list
    sum = 0             # przesłania sum (lokalnie)
    for x in list:
        sum += x
    return sum

print(total([1, 2, 3]))
print(sum([1, 2, 3]))   # poza funkcją sum działa
sum = 10                # przesłonięte w module!
print(sum([1, 2, 3]))   # int to nie funkcja → błąd


# --- Oczekiwany wynik ----------------------------------------
# 6
# 6
# TypeError: 'int' object is not callable   <- błąd zamierzony (jak na slajdzie)
