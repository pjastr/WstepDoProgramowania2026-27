"""
Wykład 6 — slajd „Cztery rodzaje wyrażeń”
Plik: 28_cztery_wyrazenia.py

Cztery rodzaje wyrażeń: listowe, zbiorowe, słownikowe i generatorowe.
"""

words = ["Ala", "ma", "kota", "a", "kot", "ma", "Ale"]
print([len(w) for w in words])              # lista
print({len(w) for w in words})              # zbiór – bez powtórzeń
print({w: len(w) for w in words})           # słownik
gen = (len(w) for w in words)               # generator – liczy na żądanie
print(type(gen).__name__, sum(gen))
# krotka: generator przekazany do tuple(); if filtruje elementy
print(tuple(w.lower() for w in words if len(w) == 3))


# --- Oczekiwany wynik ----------------------------------------
# [3, 2, 4, 1, 3, 2, 3]
# {1, 2, 3, 4}
# {'Ala': 3, 'ma': 2, 'kota': 4, 'a': 1, 'kot': 3, 'Ale': 3}
# generator 18
# ('ala', 'kot', 'ale')
