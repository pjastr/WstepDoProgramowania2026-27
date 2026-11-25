"""
Wykład 7 — slajd „Zatrzymanie na wyjątku”
Plik: 39_breakpoint_wyjatek.py

Wyjątek zgłoszony w pętli: punkt przerwania na wyjątku (Ctrl+Shift+F8 → + → Python Exception
Breakpoint → ValueError) zatrzymuje program w chwili błędu z widocznym wierszem danych.
"""

def parse_prices(lines):
    prices = {}
    for line in lines:
        name, value = line.split("=")
        prices[name.strip()] = float(value)
    return prices

data = ["chleb = 4.50", "mleko = 3.20", "masło 8.99", "ser = 12"]
print(parse_prices(data))


# --- Oczekiwany wynik ----------------------------------------
# ValueError: not enough values to unpack (expected 2, got 1)   <- błąd zamierzony (jak na slajdzie)
