"""
Wykład 7 — slajd „Każda ścieżka zwraca wartość”
Plik: 11_sciezki_return.py

Zapomniany przypadek w łańcuchu if/elif sprawia, że funkcja po cichu zwraca None.
"""

def grade(points):
    if points >= 90:
        return 5
    elif points >= 75:
        return 4
    elif points >= 50:
        return 3
    # zapomniany przypadek: points < 50

def grade_ok(points):
    if points >= 90:
        return 5
    if points >= 75:
        return 4
    if points >= 50:
        return 3
    return 2            # każda ścieżka zwraca int

print(grade(95), grade(60), grade(30), grade_ok(30))
print(grade(30) + 0.5)  # błąd daleko od przyczyny


# --- Oczekiwany wynik ----------------------------------------
# 5 3 None 2
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'float'   <- błąd zamierzony (jak na slajdzie)
