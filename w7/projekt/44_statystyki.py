"""
Wykład 7 — slajd „Ten sam program: kilka wyników”
Plik: 44_statystyki.py

Ten sam program co w C, C++, C# i Javie: funkcja zwracająca minimum, maksimum i średnią.
"""

def stats(xs):
    return min(xs), max(xs), sum(xs) / len(xs)

lo, hi, avg = stats([4, 8, 15, 16, 23, 42])
print(lo, hi, f"{avg:.2f}")


# --- Oczekiwany wynik ----------------------------------------
# 4 42 18.00
