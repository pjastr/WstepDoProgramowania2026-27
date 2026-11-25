"""
Wykład 7 — slajd „Funkcje zagnieżdżone i nonlocal”
Plik: 29_nonlocal.py

Funkcja pomocnicza zdefiniowana wewnątrz innej funkcji; nonlocal zmienia zmienną funkcji otaczającej.
"""

def report(scores):
    def fmt(s):                 # pomocnicza – lokalna
        return f"{s:.1f}"
    best = None
    def check(s):
        nonlocal best           # bez tego: UnboundLocalError
        if best is None or s > best:
            best = s
    for s in scores:
        check(s)
    return ", ".join(fmt(s) for s in scores) + " | max " + fmt(best)

print(report([3.5, 4.5, 4.0]))
fmt(1)                          # fmt nie istnieje poza report → błąd


# --- Oczekiwany wynik ----------------------------------------
# 3.5, 4.5, 4.0 | max 4.5
# NameError: name 'fmt' is not defined   <- błąd zamierzony (jak na slajdzie)
