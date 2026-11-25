"""
Wykład 7 — slajd „Kilka wyników naraz”
Plik: 10_wiele_wartosci.py

Zwracanie kilku wartości jako krotki, rozpakowanie, pomijanie wartości przez _.
"""

def stats(xs):
    n = len(xs)
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    return n, mean, var ** 0.5    # krotka

n, avg, sd = stats([2, 4, 4, 4, 5, 5, 7, 9])
print(n, avg, sd)
_, avg, _ = stats([1, 2, 3])      # _ – pomijamy
print(avg)
result = stats([1, 2, 3])         # bez rozpakowania
print(type(result).__name__, result[1])
q, r = divmod(17, 5)              # wbudowany przykład
print(q, r)
n, avg = stats([1, 2])            # 3 wartości, 2 nazwy


# --- Oczekiwany wynik ----------------------------------------
# 8 5.0 2.0
# 2.0
# tuple 2.0
# 3 2
# ValueError: too many values to unpack (expected 2)   <- błąd zamierzony (jak na slajdzie)
