"""
Wykład 6 — slajd „namedtuple — krotka z nazwanymi polami”
Plik: 03_namedtuple.py

namedtuple — krotka z nazwanymi polami (p.x zamiast p[0]).
"""

from collections import namedtuple

# nowy typ: nazwa typu i nazwy pól
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
# pole po nazwie, po indeksie; porównanie ze zwykłą krotką
print(p, p.x, p[1], p == (3, 4))
q = p._replace(x=0)                # nowa krotka ze zmienionym x
print(q, q._asdict())              # _asdict – konwersja na słownik
# najwyżej położony punkt – kluczem jest współrzędna y
print(max([Point(1, 5), Point(2, 1)], key=lambda pt: pt.y))
p.x = 7                            # krotka jest niezmienna → błąd


# --- Oczekiwany wynik ----------------------------------------
# Point(x=3, y=4) 3 4 True
# Point(x=0, y=4) {'x': 0, 'y': 4}
# Point(x=1, y=5)
# AttributeError: can't set attribute   <- błąd zamierzony (jak na slajdzie)
