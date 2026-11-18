"""
Wykład 6 — slajd „frozenset — zbiór niezmienny”
Plik: 10_frozenset.py

frozenset — niezmienny (i haszowalny) zbiór: zbiór zbiorów, klucz słownika.
"""

fs = frozenset("abc")
print(fs == set("cab"), "a" in fs)   # porównanie ze zwykłym zbiorem
# zbiór zbiorów – kolejność osób w parze nie ma znaczenia
teams = {frozenset({"Ala", "Ola"}), frozenset({"Ola", "Ala"})}
print(len(teams))                    # to ta sama para
# krawędź grafu nieskierowanego {u, v} → waga
edges = {frozenset({1, 2}): 7, frozenset({2, 3}): 4}
print(edges[frozenset({2, 1})])
print(type(fs | {"d"}).__name__)     # typ wyniku = typ lewego argumentu
fs.add("d")                          # niezmienny → brak metody add


# --- Oczekiwany wynik ----------------------------------------
# True True
# 1
# 7
# frozenset
# AttributeError: 'frozenset' object has no attribute 'add'   <- błąd zamierzony (jak na slajdzie)
