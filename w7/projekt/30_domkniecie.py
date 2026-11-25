"""
Wykład 7 — slajd „Domknięcie”
Plik: 30_domkniecie.py

Funkcja wewnętrzna zwrócona na zewnątrz pamięta zmienne funkcji, w której powstała.
"""

def make_multiplier(k):
    def multiply(x):
        return x * k        # k z funkcji otaczającej
    return multiply         # funkcja, nie wynik

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))
print(double.__closure__[0].cell_contents)

def make_counter():
    count = 0
    def increment():
        nonlocal count      # stan między wywołaniami
        count += 1
        return count
    return increment

c1, c2 = make_counter(), make_counter()
print(c1(), c1(), c1(), c2())  # osobne liczniki


# --- Oczekiwany wynik ----------------------------------------
# 10 15
# 2
# 1 2 3 1
