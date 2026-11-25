"""
Wykład 7 — slajd „Warunkowy punkt przerwania”
Plik: 38_warunkowy_breakpoint.py

Funkcja z błędem w regule lat przestępnych. Punkt przerwania w wierszu if is_leap(year)
z warunkiem  year % 100 == 0  zatrzyma program tylko 3 razy zamiast 201.
"""

def is_leap(year):      # błąd: brak reguły 400
    return year % 4 == 0 and year % 100 != 0

def count_leap(start, stop):
    count = 0
    for year in range(start, stop + 1):
        if is_leap(year):   # warunek: year % 100 == 0
            count += 1
    return count

print(count_leap(1900, 2100))   # oczekiwane 49
print(is_leap(2000), is_leap(2024), is_leap(1900))


# --- Oczekiwany wynik ----------------------------------------
# 48
# False True False
