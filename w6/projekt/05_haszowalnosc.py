"""
Wykład 6 — slajd „Haszowalność a niezmienność”
Plik: 05_haszowalnosc.py

Które obiekty są haszowalne (mogą być kluczem słownika / elementem zbioru)?
"""

grid = {(1, 2): "A"}        # krotka jako klucz
print(grid[(1, 2)], (1, 2) in grid)
# kolejność w zbiorze nie ma znaczenia
a, b = frozenset({1, 2}), frozenset({2, 1})
print(hash(a) == hash(b))
# sprawdzamy, które obiekty mają hash
for obj in [(1, 2), (1, [2]), "ab",
            frozenset(), {1}, {}]:
    try:
        hash(obj)           # może zgłosić TypeError
        print(type(obj).__name__, "hashable")
    except TypeError:
        print(type(obj).__name__, "unhashable")


# --- Oczekiwany wynik ----------------------------------------
# A True
# True
# tuple hashable
# tuple unhashable
# str hashable
# frozenset hashable
# set unhashable
# dict unhashable
