"""
Wykład 6 — slajd „Zbiór — podstawy”
Plik: 06_zbior_podstawy.py

Zbiór: brak duplikatów, brak indeksów, szybki test „czy należy?”.
"""

s = {3, 1, 4, 1, 5, 9, 2, 6, 5}     # duplikaty znikają
print(s, len(s))
# zbiór liter napisu – każda litera tylko raz
print(set("mississippi") == {"m", "i", "s", "p"})
print(type({}).__name__, type(set()).__name__)   # {} to słownik!
print(4 in s, 7 not in s)           # test przynależności – średnio O(1)
print(sorted(set("banana")))        # sorted zwraca posortowaną listę
s[0]                                # zbiór nie ma indeksów → błąd


# --- Oczekiwany wynik ----------------------------------------
# {1, 2, 3, 4, 5, 6, 9} 7
# True
# dict set
# True True
# ['a', 'b', 'n']
# TypeError: 'set' object is not subscriptable   <- błąd zamierzony (jak na slajdzie)
