"""
Wykład 7 — slajd „Wartości domyślne”
Plik: 14_wartosci_domyslne.py

Parametry z wartościami domyślnymi — także w funkcjach wbudowanych.
"""

def greet(name, greeting="Cześć", punct="!"):
    return f"{greeting}, {name}{punct}"

print(greet("Ola"))
print(greet("Jan", "Dzień dobry"))
print(greet("Ewa", punct="?"))  # pomijamy środkowy
print(round(3.14159), round(3.14159, 2))
print("a-b-c".split("-", maxsplit=1))


# --- Oczekiwany wynik ----------------------------------------
# Cześć, Ola!
# Dzień dobry, Jan!
# Cześć, Ewa?
# 3 3.14
# ['a', 'b-c']
