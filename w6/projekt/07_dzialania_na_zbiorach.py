"""
Wykład 6 — slajd „Działania na zbiorach”
Plik: 07_dzialania_na_zbiorach.py

Działania na zbiorach: suma |, część wspólna &, różnica -, różnica symetryczna ^.
"""

a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a | b, a & b)         # suma, część wspólna
print(a - b, b - a, a ^ b)  # różnice, różn. symetr.
# podzbiór, podzbiór właściwy, rozłączność
print({1, 2} <= a, a < a, a.isdisjoint({7, 8}))


# --- Oczekiwany wynik ----------------------------------------
# {1, 2, 3, 4, 5} {3, 4}
# {1, 2} {5} {1, 2, 5}
# True False True
