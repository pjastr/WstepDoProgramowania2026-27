"""
Wykład 7 — slajd „Rozpakowanie przy wywołaniu”
Plik: 18_rozpakowanie_wywolanie.py

* i ** w wywołaniu rozpakowują listę/krotkę i słownik na osobne argumenty.
"""

def volume(a, b, c):
    return a * b * c

dims = [2, 3, 4]
print(volume(*dims))        # volume(2, 3, 4)
opts = {"b": 3, "c": 4}
print(volume(2, **opts))    # volume(2, b=3, c=4)
print(*"abc", sep="-")      # print(*args, sep=…)
rows = [(1, "a"), (2, "b")]
print(*rows, sep="\n")      # wiersz na element
volume(*[1, 2])             # za mało → błąd


# --- Oczekiwany wynik ----------------------------------------
# 24
# 24
# a-b-c
# (1, 'a')
# (2, 'b')
# TypeError: volume() missing 1 required positional argument: 'c'   <- błąd zamierzony (jak na slajdzie)
