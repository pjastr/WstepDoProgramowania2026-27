"""
Wykład 6 — slajd „Widoki i zmiany w trakcie iteracji”
Plik: 16_widoki_slownika.py

Widoki keys()/items() i zmiana słownika w trakcie pętli.
"""

d = {"a": 1, "b": 0, "c": 2}
keys = d.keys()                      # widok, nie kopia
d["e"] = 0
print(keys, len(keys))               # widok widzi nowy klucz "e"
print(keys & {"a", "z"}, keys - {"a", "b", "c"})   # jak na zbiorach
for k in list(d):                    # migawka kluczy – można usuwać
    if d[k] == 0:
        del d[k]
print(d)
for k in d:                          # pętla po samym słowniku...
    d[k + "!"] = 0                   # ...i dodawanie kluczy → RuntimeError


# --- Oczekiwany wynik ----------------------------------------
# dict_keys(['a', 'b', 'c', 'e']) 4
# {'a'} {'e'}
# {'a': 1, 'c': 2}
# RuntimeError: dictionary changed size during iteration   <- błąd zamierzony (jak na slajdzie)
