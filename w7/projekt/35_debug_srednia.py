"""
Wykład 7 — slajd „Punkt przerwania i tryb Debug”
Plik: 35_debug_srednia.py

Funkcja z błędem do znalezienia debugerem: postaw punkt przerwania w wierszu z kept,
uruchom Debug (Shift+F9) i obejrzyj zmienne ys, kept, k w panelu Variables.
"""

def trimmed_mean(xs, k):
    """Średnia bez k najmniejszych i k największych."""
    ys = sorted(xs)
    kept = ys[k:-k]             # ← punkt przerwania
    return sum(kept) / len(kept)

print(trimmed_mean([7, 1, 5, 9, 3], 1))
print(trimmed_mean([7, 1, 5, 9, 3], 0))


# --- Oczekiwany wynik ----------------------------------------
# 5.0
# ZeroDivisionError: division by zero   <- błąd zamierzony (jak na slajdzie)
