"""
Wykład 6 — slajd „Grupowanie”
Plik: 19_grupowanie.py

Grupowanie: klucz → lista elementów (setdefault i defaultdict).
"""

words = ["apple", "avocado", "banana", "blueberry", "cherry"]
groups = {}
for w in words:
    # pierwsza litera → lista słów (pusta lista, gdy klucza brak)
    groups.setdefault(w[0], []).append(w)
print(groups)
from collections import defaultdict
by_len = defaultdict(list)       # brakujący klucz → nowa pusta lista
for w in words:
    by_len[len(w)].append(w)     # bez sprawdzania, czy klucz istnieje
print(dict(by_len))
print(by_len[3], len(by_len))    # sam odczyt dodał klucz 3!


# --- Oczekiwany wynik ----------------------------------------
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
# {5: ['apple'], 7: ['avocado'], 6: ['banana', 'cherry'], 9: ['blueberry']}
# [] 5
