"""
Wykład 7 — slajd „Funkcja czysta a efekty uboczne”
Plik: 12_czyste_funkcje.py

Funkcja czysta zwraca nowy obiekt; funkcja z efektem ubocznym zmienia argument.
"""

def with_item(cart, item):      # czysta: nowa lista
    return cart + [item]

def add_item(cart, item):       # efekt uboczny
    cart.append(item)
    return len(cart)

cart = ["chleb"]
print(with_item(cart, "mleko"), cart)
print(add_item(cart, "mleko"), cart)
print(add_item(cart, "mleko"), cart)  # inny wynik!


# --- Oczekiwany wynik ----------------------------------------
# ['chleb', 'mleko'] ['chleb']
# 2 ['chleb', 'mleko']
# 3 ['chleb', 'mleko', 'mleko']
