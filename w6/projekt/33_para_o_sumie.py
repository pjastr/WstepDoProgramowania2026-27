"""
Wykład 6 — slajd „Studium: para o zadanej sumie”
Plik: 33_para_o_sumie.py

Studium: para elementów o zadanej sumie — O(n²) kontra O(n) ze słownikiem.
"""

def pair_sum_slow(xs, target):      # O(n^2)
    # sprawdzamy każdą parę i < j
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] + xs[j] == target:
                return i, j
    return None

def pair_sum(xs, target):           # O(n)
    seen = {}                       # wartość → indeks
    for j, x in enumerate(xs):
        # czy dopełnienie już było?
        if target - x in seen:
            return seen[target - x], j
        seen[x] = j                 # zapamiętaj x
    return None

xs = [8, 3, 11, 5, 2, 7]
# obie wersje – ten sam wynik
print(pair_sum_slow(xs, 9),
      pair_sum(xs, 9))
print(pair_sum(xs, 14),
      pair_sum(xs, 100))


# --- Oczekiwany wynik ----------------------------------------
# (4, 5) (4, 5)
# (1, 2) None
