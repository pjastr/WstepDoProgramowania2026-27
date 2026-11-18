"""
Wykład 6 — slajd „Metody, operatory, modyfikacja”
Plik: 08_metody_zbioru.py

Metody zbioru i modyfikacja w miejscu: add, update, discard, remove, |=, &=, -=.
"""

a = {1, 2, 3}
# metoda przyjmuje dowolne iterowalne
print(a.union([3, 4], range(5, 7)))
a.add(10)               # jeden element
a.update("xy")          # każdy znak osobno
a.discard(99)           # brak: bez błędu
a -= {"x", "y"}         # różnica w miejscu
print(a)
a &= {1, 2, 10}         # część wspólna w miejscu
print(a)
a.remove(99)            # brak: KeyError


# --- Oczekiwany wynik ----------------------------------------
# {1, 2, 3, 4, 5, 6}
# {1, 2, 3, 10}
# {1, 2, 10}
# KeyError: 99   <- błąd zamierzony (jak na slajdzie)
