"""
Wykład 7 — slajd „Zadania (2/2)”
Plik: 43_zadanie8_recenzja.py

Zadanie 8 (Recenzja): ta funkcja zawiera kilka błędów — znajdź je i popraw.
Dopisz na dole wywołania, np. print(summary([3, 1, 3])) dwa razy z rzędu, i sprawdź, co się dzieje.
Użyj debugera.
"""

count = 0

def summary(values, precision=2, seen=[]):
    for v in values:
        if v not in seen:
            seen.append(v)
            count += 1
    avg = round(sum(values) / len(values), precision)
    print(f"średnia: {avg}, różnych: {count}")
