"""
Wykład 7 — slajd „Parametry i argumenty”
Plik: 13_parametry_argumenty.py

Parametr (w definicji) a argument (w wywołaniu); argumenty pozycyjne i nazwane.
"""

def power(base, exponent):     # parametry
    return base ** exponent

print(power(2, 10))            # pozycyjne
print(power(exponent=2, base=10))  # nazwane
print(power(3, exponent=3))    # pozycyjny, nazwany
power(2)                       # brak argumentu → błąd


# --- Oczekiwany wynik ----------------------------------------
# 1024
# 100
# 27
# TypeError: power() missing 1 required positional argument: 'exponent'   <- błąd zamierzony (jak na slajdzie)
