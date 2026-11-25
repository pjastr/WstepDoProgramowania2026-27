"""
Wykład 7 — slajd „Brak return → None”
Plik: 08_brak_return.py

Funkcja bez return (lub z samym return) zwraca None.
"""

def add_vat(price):
    price * 1.23          # obliczone… i wyrzucone

def greet(name):
    print("Cześć,", name) # wypisuje, nic nie zwraca

print(add_vat(100))
r = greet("Ola")
print(r, type(r).__name__)
x = print("tekst")        # print też zwraca None
print(x)
print(len("abc"), [3, 1, 2].sort())  # sort → None


# --- Oczekiwany wynik ----------------------------------------
# None
# Cześć, Ola
# None NoneType
# tekst
# None
# 3 None
