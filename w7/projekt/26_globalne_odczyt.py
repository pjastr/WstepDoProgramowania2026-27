"""
Wykład 7 — slajd „Odczyt zmiennych globalnych”
Plik: 26_globalne_odczyt.py

Funkcja może czytać zmienne modułu; wartość jest pobierana w chwili wywołania, nie definicji.
"""

VAT = 0.23

def gross(net):
    return round(net * (1 + VAT), 2)  # odczyt

print(gross(100))
VAT = 0.08              # zmiana zmiennej globalnej
print(gross(100))       # …zmienia wynik funkcji

def show_limit():
    print("limit:", limit)  # przy def jeszcze brak

limit = 10              # istnieje przy wywołaniu
show_limit()


# --- Oczekiwany wynik ----------------------------------------
# 123.0
# 108.0
# limit: 10
