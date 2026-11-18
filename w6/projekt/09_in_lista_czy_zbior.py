"""
Wykład 6 — slajd „in: lista czy zbiór?”
Plik: 09_in_lista_czy_zbior.py

Porównanie czasu operacji `in` dla listy i zbioru (pomiar timeit).

Uwaga: czasy zależą od komputera — liczy się to, jak rosną z n.
"""

from timeit import timeit
for n in [1_000, 10_000, 100_000]:
    as_list = list(range(n))
    as_set = set(as_list)          # te same dane w zbiorze
    # 1000 razy szukamy OSTATNIEGO elementu – najgorszy przypadek dla listy
    t_list = timeit(lambda: n - 1 in as_list, number=1000)
    t_set = timeit(lambda: n - 1 in as_set, number=1000)
    print(f"n = {n:>7}: list {t_list * 1000:8.2f} ms, set {t_set * 1000:5.3f} ms")


# --- Oczekiwany wynik ----------------------------------------
# n =    1000: list     4.11 ms, set 0.044 ms
# n =   10000: list    41.39 ms, set 0.042 ms
# n =  100000: list   459.84 ms, set 0.038 ms
