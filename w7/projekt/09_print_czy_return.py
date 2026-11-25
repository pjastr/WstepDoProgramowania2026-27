"""
Wykład 7 — slajd „print czy return?”
Plik: 09_print_czy_return.py

Funkcja, która wypisuje wynik, a funkcja, która go zwraca — tylko zwrócony wynik można dalej liczyć.
"""

def area_print(a, b):
    print(a * b)        # wynik tylko na ekran

def area(a, b):
    return a * b        # wynik dla wywołującego

total = area(2, 3) + area(4, 5)
print(total)
total = area_print(2, 3) + area_print(4, 5)


# --- Oczekiwany wynik ----------------------------------------
# 26
# 6
# 20
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'   <- błąd zamierzony (jak na slajdzie)
