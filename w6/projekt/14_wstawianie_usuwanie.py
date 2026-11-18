"""
Wykład 6 — slajd „Wstawianie, łączenie, usuwanie”
Plik: 14_wstawianie_usuwanie.py

Wstawianie, łączenie i usuwanie: update, |, pop, popitem, del.
"""

d = {"a": 1, "b": 2}
d.update({"b": 20, "c": 3}, d=4)        # nadpisuje "b", dodaje "c" i "d"
print(d)
defaults = {"color": "red", "size": 10}
user = {"size": 12}
print(defaults | user, user | defaults)     # wygrywa prawa strona
# pop – usuń i zwróć; popitem – ostatnio wstawiony wpis
print(d.pop("a"), d.pop("zz", None), d.popitem())
del d["b"]                              # usuwa bez zwracania
print(d)
d.pop("zz")                             # brak klucza i brak domyślnej → KeyError


# --- Oczekiwany wynik ----------------------------------------
# {'a': 1, 'b': 20, 'c': 3, 'd': 4}
# {'color': 'red', 'size': 12} {'size': 10, 'color': 'red'}
# 1 None ('d', 4)
# {'c': 3}
# KeyError: 'zz'   <- błąd zamierzony (jak na slajdzie)
